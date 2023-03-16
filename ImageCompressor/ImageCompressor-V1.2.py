"""
This script is to reduce image file size with below terms
1. Ratio 0.6 & quality 75 to the images above 0.6mb
2. Ratio 0.6 & quality 90 to the images <= 0.6mb
3. Current version handles JPEG, JPG, PNG, PJP, PJPEG, JFIF and GIF

Usage:
1.Run the Program by passing appropriate commandline arguments
syntax : program.py source_image|source_dir destination_directory optional arguments
Adding -j : Converts to jpeg format irrespective of its original format
Skipping -j : Retains original format
"""

__author__ = "Doddahulugappa Barikara"
__license__ = "GPL"
__version__ = "1.2"
__maintainer__ = "Doddahulugappa Barikara"

import glob
import argparse
import logging
from logging.handlers import RotatingFileHandler
import os
import re
from PIL import Image

THRESHOLD = 600000  # Images less than 0.6 mb has different conversion ratio

# ==================== Logging setup ====================== #
log_file = "ImageCompressorLog.log"  # Log File Path
handler = [RotatingFileHandler(log_file,
                               mode='a',
                               maxBytes=5000000,  # 5 MB
                               backupCount=5,  # Keeps last 5 log files max
                               encoding=None,
                               delay=False,
                               errors=None,

                               )]  # Rotational logging

message_format = "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"  # Message format
logging.basicConfig(format=message_format, level=logging.DEBUG, handlers=handler)


def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    :param b:
    :param factor:
    :param suffix:
    :return:
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"


def compress_img(
        image_name,
        destination="",
        saveas_file="",
        new_size_ratio=0.6,
        quality=75,
        width=None,
        height=None,
        to_jpg=True):
    """

    :param image_name:
    :param destination:
    :param saveas_file:
    :param new_size_ratio:
    :param quality:
    :param width:
    :param height:
    :param to_jpg:
    :return:
    """
    try:
        # load the image to memory
        img = Image.open(image_name)

        # log old image shape
        logging.info(f"[+] Old Image shape {img.size}")

        # get the original image size in bytes
        image_size = os.path.getsize(image_name)

        # log the size before compression/resizing
        logging.info(f"[*] Size before compression:{get_size_format(image_size)}")

        if new_size_ratio < 1.0 and image_size > THRESHOLD:
            # if resizing ratio is below 1.0, then multiply width & height with
            # this ratio to reduce image size
            img = img.resize((int(img.size[0] *
                                  new_size_ratio), int(img.size[1] *
                                                       new_size_ratio)))

        elif width and height:
            # if width and height are set, resize with them instead
            img = img.resize((width, height))

            # log new image shape
            logging.info(f"[+] New Image shape:{img.size}")

        # split the filename and extension
        filename, ext = os.path.splitext(image_name)

        path, filename = os.path.split(filename)

        if to_jpg:
            # change the extension to JPEG
            ext = ".jpg"

        if saveas_file:  # if its individual file
            new_filename = os.path.join(destination, saveas_file + ext)

        else:  # in case of bulk images
            new_filename = f"{filename}{ext}"
            new_filename = os.path.join(path, destination, new_filename)
        try:
            # save the image with the corresponding quality and optimize set to True
            if image_size <= THRESHOLD:
                quality = 90
            img.save(new_filename, quality=quality, optimize=True)

        except OSError:
            # convert the image to RGB mode first
            img = img.convert("RGB")
            # save the image with the corresponding quality and optimize set to True
            img.save(new_filename, quality=quality, optimize=True)

        # get the new image size in bytes
        new_image_size = os.path.getsize(new_filename)

        # log the new size in a good format
        logging.info(f"[+] Size after compression:{get_size_format(new_image_size)}")

        # calculate the saving bytes
        saving_diff = new_image_size - image_size

        # log the saving percentage
        logging.info(f"[+] Image size change: {saving_diff / image_size * 100:.2f}% of the original image size.")

        if destination == "":
            logging.info(f"Image has been compressed & saved!")

    except Exception as e:
        logging.error(f"Error has occurred {e}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Simple Python script for compressing and resizing images")
    parser.add_argument("image", help="Target image name or path to compress and/or resize")
    parser.add_argument("destination", help="Destination directory to store compressed image")
    parser.add_argument("-j", "--to-jpg", action="store_true", help="Whether to convert the image to the JPEG format")
    parser.add_argument("-q", "--quality", type=int,
                        help="Quality ranging from a minimum of 0 (worst) to a maximum of 95 (best). Default is 75",
                        default=75)
    parser.add_argument("-r", "--resize-ratio", type=float,
                        help="Resizing ratio from 0 to 1, setting to 0.5 will multiply width & height of the image by "
                             "0.5. Default is 0.6",
                        default=0.6)
    parser.add_argument("-w", "--width", type=int,
                        help="The new width image, make sure to set it with the `height` parameter")
    parser.add_argument("-hh", "--height", type=int,
                        help="The new height for the image, make sure to set it with the `width` parameter")

    args = parser.parse_args()

    try:
        isFile = os.path.isfile(args.image)  # Check target is file or path
        if isFile:
            if args.image.lower().endswith(('.png', '.jpg', '.jpeg', '.jfif', '.gif', '.jpeg', '.pjpeg', '.pjp')):
                file_path, file_name = os.path.split(args.image)
                logging.info(f"{args.image}")
                save_as_file = file_name.split(".")[0]
                compress_img(args.image, saveas_file=save_as_file, destination=args.destination, to_jpg=args.to_jpg,
                             quality=args.quality, new_size_ratio=args.resize_ratio, height=args.height,
                             width=args.width)
            else:
                logging.warning("Not a image file")
        else:
            # Get all files from target directory
            files = glob.glob(args.image + "/*.*",
                              recursive=False)

            # Filter all image files
            files = [file for file in files if re.search("png|jpg|jpeg|jfif|pjp|pjpeg|gif", file, re.IGNORECASE)]

            # Loop through all image files and call compress_img method
            for file in files:
                logging.info(f"{file}")
                compress_img(file, destination=args.destination, to_jpg=args.to_jpg, quality=args.quality,
                             new_size_ratio=args.resize_ratio, height=args.height, width=args.width)
            if not files:
                logging.warning("No Image files found")
    except Exception as e:
        logging.error(f"Error has occurred {e}")

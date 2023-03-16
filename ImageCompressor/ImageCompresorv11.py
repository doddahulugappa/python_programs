"""
This script is to reduce image file size with below terms
1. Ratio 0.6 & quality 75 to the images above 0.6mb
2. Ratio 0.6 & quality 90 to the images <= 0.6mb
3. Current version handles JPEG, JPG, PNG, PJP, PJPEG, JFIF and GIF

Usage:
1.Run the Program by passing appropriate commandline arguments
syntax : program.py b64encodedstr optional arguments
Converts to jpeg default
"""

__author__ = "Doddahulugappa Barikara"
__license__ = "GPL"
__version__ = "1.1"
__maintainer__ = "Doddahulugappa Barikara"

import base64
import argparse
import io
from PIL import Image
from PIL.Image import Resampling

THRESHOLD = 600000  # Images less than 0.6 mb has different conversion ratio


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
        b64encode_str,
        new_size_ratio=0.6,
        quality=75,
        width=None,
        height=None,
        ext="JPEG"):
    """

    :param b64encode_str:
    :param new_size_ratio:
    :param quality:
    :param width:
    :param height:
    :param ext:
    :return:
    """

    compressed_b64_en_str = b''  # empty b64 string
    try:
        # Decode encoded base64 string
        img_data = base64.b64decode(b64encode_str)

        # load the image to buffer memory
        img = Image.open(io.BytesIO(img_data))

        # print old image shape
        print("[+] Old Image shape:", img.size)

        # get the original image size in bytes
        image_size = (len(b64encode_str) * 6) / 8

        # print the size before compression/resizing
        print("[*] Size before compression:", get_size_format(image_size))

        if new_size_ratio < 1.0 and image_size > THRESHOLD:
            # if resizing ratio is below 1.0, then multiply width & height with
            # this ratio to reduce image size
            img = img.resize((int(img.size[0] *
                                  new_size_ratio), int(img.size[1] *
                                                       new_size_ratio)))

        elif width and height:
            # if width and height are set, resize with them instead
            img = img.resize((width, height))

            # print new image shape
            print("[+] New Image shape:", img.size)

        buffered = io.BytesIO()
        try:
            # save the image with the corresponding quality and optimize set to True

            if image_size <= THRESHOLD:
                quality = 90

            img.save(buffered, format=ext, quality=quality, optimize=True)
            compressed_b64_en_str = base64.b64encode(buffered.getvalue())

        except OSError:
            # convert the image to RGB mode first
            img = img.convert("RGB")
            # save the image with the corresponding quality and optimize set to True
            img.save(buffered, format=ext, quality=quality, optimize=True)
            compressed_b64_en_str = base64.b64encode(buffered.getvalue())

        # get the new image size in bytes
        new_image_size = (len(compressed_b64_en_str) * 6) / 8

        # print the new size in a good format
        print("[+] Size after compression:", get_size_format(new_image_size))

        # calculate the saving bytes
        saving_diff = new_image_size - image_size

        # print the saving percentage
        print(
            f"[+] Image size change: {saving_diff / image_size * 100:.2f}% of the original image size.")

    except Exception as e:
        print(f"Error has occurred {e}")

    return compressed_b64_en_str


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Simple Python script for compressing and resizing images")
    parser.add_argument("base64", help="Target image base64 encoded string")
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

    print("=" * 50)
    print("[*] Base64:", args.base64)
    print("[*] Quality:", args.quality)
    print("[*] Resizing ratio:", args.resize_ratio)
    if args.width and args.height:
        print("[*] Width:", args.width)
        print("[*] Height:", args.height)
    print("=" * 50)
    compressed_encoded_b64_str = compress_img(args.base64,
                                              quality=args.quality,
                                              new_size_ratio=args.resize_ratio,
                                              height=args.height,
                                              width=args.width)

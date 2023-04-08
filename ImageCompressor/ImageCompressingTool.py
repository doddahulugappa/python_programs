"""
This script is to reduce image file size with below terms
1. ratio 0.6 & qulaity 75 to the images above 0.6mb
2. ration 0.6 & qulaity 90 to the images <= 0.6mb
3. It converts all JPEG,JPG,PNG,PJP,JFIF, GIF to JPG

Usage:
1.Run the tool
2.Select Source Dir
3 Selct Dest Dir
"""

__author__ = "Doddahulugappa Barikara"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Doddahulugappa Barikara"

import glob
import re
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import os
from PIL import Image
from PIL.Image import Resampling

threshold = 600000


def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"


def compress_img(
        image_name,
        destination="",
        new_size_ratio=0.6,
        quality=75,
        width=None,
        height=None,
        to_jpg=True):
    try:
        # load the image to memory
        img = Image.open(image_name)
        # print the original image shape
        print("[*] Image shape:", img.size)
        # get the original image size in bytes
        image_size = os.path.getsize(image_name)
        # print the size before compression/resizing
        print("[*] Size before compression:", get_size_format(image_size))
        if new_size_ratio < 1.0 and image_size > threshold:
            # if resizing ratio is below 1.0, then multiply width & height with
            # this ratio to reduce image size
            img = img.resize((int(img.size[0] *
                                  new_size_ratio), int(img.size[1] *
                                                       new_size_ratio)), Resampling.LANCZOS)
            # print new image shape
            print("[+] New Image shape:", img.size)
        elif width and height:
            # if width and height are set, resize with them instead
            img = img.resize((width, height), Image.ANTIALIAS)
            # print new image shape
            print("[+] New Image shape:", img.size)
        # split the filename and extension
        filename, ext = os.path.splitext(image_name)

        path, filename = os.path.split(filename)
        # make new filename appending _compressed to the original file name
        if to_jpg:
            # change the extension to JPEG
            new_filename = f"{filename}_compressed.jpg"
        else:
            # retain the same extension of the original image
            new_filename = f"{filename}_compressed{ext}"
        new_filename = os.path.join(path, destination, new_filename)
        try:
            # save the image with the corresponding quality and optimize set to
            # True
            if image_size <= threshold:
                quality = 90
            img.save(new_filename, quality=quality, optimize=True)

        except OSError:
            # convert the image to RGB mode first
            img = img.convert("RGB")
            # save the image with the corresponding quality and optimize set to
            # True
            img.save(new_filename, quality=quality, optimize=True)
        # get the new image size in bytes
        new_image_size = os.path.getsize(new_filename)
        # print the new size in a good format
        print("[+] Size after compression:", get_size_format(new_image_size))
        # calculate the saving bytes
        saving_diff = new_image_size - image_size
        # print the saving percentage
        print(
            f"[+] Image size change: {saving_diff/image_size*100:.2f}% of the original image size.")
    except Exception as e:
        print(e)


root = Tk()
root.withdraw()

try:
    source_folder = filedialog.askdirectory(title="Select Source Directory")
    destination_folder = filedialog.askdirectory(
        title="Select Destination Directory")

    files = glob.glob(source_folder + "/*.*",
                      recursive=False)

    files = [
        file for file in files if re.search(
            "png|jpg|jpeg|jfif|pjp|pjpeg|gif",
            file,
            re.IGNORECASE)]

    if not files:
        messagebox.showwarning("No Files Found", "No Image Files Found")
    else:
        for file in files:
            compress_img(file, destination_folder)
        messagebox.showinfo(
            "Completed",
            "Images have been compressed & saved in destination dir\n" +
            destination_folder)
except Exception as e:
    print(e)

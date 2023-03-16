"""
This script is to reduce image file size with below terms
1. ratio 0.6 & quality 75 to the images above 0.6mb
2. ration 0.6 & quality 90 to the images <= 0.6mb
3. It converts all JPEG,JPG,PNG,PJP,JFIF, GIF to JPG

Usage:
1.Run the tool
2.Select Source Dir
3 Select Destination Dir
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
from tkinter.filedialog import asksaveasfile

from PIL import Image, ImageTk
from PIL.Image import Resampling

THRESHOLD = 600000  # Images less than 0.6 mb has different conversion ratio


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
        # print the original image shape
        print("[*] Image shape:", img.size)
        # get the original image size in bytes
        image_size = os.path.getsize(image_name)
        # print the size before compression/resizing
        print("[*] Size before compression:", get_size_format(image_size))
        if new_size_ratio < 1.0 and image_size > THRESHOLD:
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
        if saveas_file:
            new_filename = saveas_file

        # make new filename appending _compressed to the original file name
        else:
            if to_jpg:
                # change the extension to JPEG
                new_filename = f"{filename}__1.jpg"
            else:
                # retain the same extension of the original image
                new_filename = f"{filename}__1{ext}"
            new_filename = os.path.join(path, destination, new_filename)
        try:
            # save the image with the corresponding quality and optimize set to
            # True
            if image_size <= THRESHOLD:
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
            f"[+] Image size change: {saving_diff / image_size * 100:.2f}% of the original image size.")

        if destination == "":
            message_text = "Image has been compressed & saved!"
            messagebox.showinfo("Completed",
                                message_text)
    except Exception as e:
        print(e)
        messagebox.showwarning("Warning",
                               "Some error has occurred! Try Again")


def open_file():
    file_path = filedialog.askopenfilename(
        title="Select the Image file", filetypes=[
            ('Image File', '.jpg .png .jpeg .jfif .pjp .pjpeg .gif')])
    if file_path:
        print(f"{file_path}")
        path, file_name = os.path.split(file_path)
        # Show save as file dialog to for single file conversion
        saveas_file = asksaveasfile(
            initialfile=file_name.split(".")[0] +
            "_1",
            title='Select dir & Rename the file',
            defaultextension=".jpg",
            filetypes=[
                ("JPG",
                 ".jpg"),
                ("PNG",
                 ".png"),
                ("GIF",
                 ".gif")])

        if saveas_file:
            compress_img(file_path, saveas_file=saveas_file.name)


def open_dir():
    try:
        source_folder = filedialog.askdirectory(
            title="Select Source Directory")
        if source_folder:
            destination_folder = filedialog.askdirectory(
                title="Select Destination Directory")
            if destination_folder:
                files = glob.glob(source_folder + "/*.*",
                                  recursive=False)

                files = [
                    file for file in files if re.search(
                        "png|jpg|jpeg|jfif|pjp|pjpeg|gif",
                        file,
                        re.IGNORECASE)]

                if not files:
                    messagebox.showwarning(
                        "No Files Found", "No Image Files Found")
                else:
                    for file in files:
                        compress_img(file, destination_folder)
                    messagebox.showinfo(
                        "Completed",
                        "Images have been compressed & saved in destination dir\n" +
                        destination_folder)
    except Exception as e:
        print(e)


root = Tk()
# root.withdraw()

# set the background colour of GUI window
root.configure(background='gray')

icon_photo = r"C:\Users\Barikara\Desktop\Pot\ImageCompress1.ico"

icon_photo = ImageTk.PhotoImage(Image.open(icon_photo))  # PIL solution

root.iconphoto(False, icon_photo)

# set the title of GUI window
root.title("Image Compressor")

# root.geometry("270x280")
root.geometry("")

# create a Form label
heading = Label(
    root,
    text="Image Compressing Tool",
    bg="light blue",
    font=(
        "default",
         12))

file_select = Button(root, text="Browse File", command=open_file)

dir_select = Button(root, text="Browse Folder", command=open_dir)

heading.grid(
    row=1,
    column=1,
    ipadx="30",
    ipady="10",
    padx=15,
    pady=10,
    columnspan=2)

file_select.grid(
    row=2,
    column=1,
    ipadx="30",
    ipady="10",
    padx=35,
    pady=10,
    columnspan=3)

dir_select.grid(
    row=3,
    column=1,
    ipadx="30",
    ipady="10",
    padx=35,
    pady=10,
    columnspan=3)

exit_button = Button(root, text="Exit", background="light yellow",
                     foreground="black", command=root.destroy)
exit_button.grid(
    row=4,
    column=1,
    ipadx="30",
    ipady="10",
    padx=35,
    pady=10,
    columnspan=2)

# start the GUI
root.mainloop()

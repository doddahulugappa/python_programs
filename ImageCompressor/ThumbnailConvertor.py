import glob
import os
import re
from multiprocessing import Pool, Process
import time

from PIL import Image
import matplotlib.pyplot as plt


def convert_to_thumbnail(file):
    img = Image.open(file)

    SIZE = (75, 75)

    img.thumbnail(SIZE)

    path, name = os.path.split(file)

    img.save(r'D:\\dest'+ "\\" + name)


def convert_to_thumbnail_process(files):
    for file in files:
        img = Image.open(file)

        SIZE = (75, 75)

        img.thumbnail(SIZE)

        path, name = os.path.split(file)

        img.save(r'D:\\dest' + "\\" + name)


if __name__ == "__main__":
    files = glob.glob(r"D://source" + "/*.*", recursive=False)
    files = [file for file in files if re.search("png|jpg|jpeg|jfif|pjp|pjpeg|gif", file, re.IGNORECASE)]

    start = time.time()
    for file in files:
        convert_to_thumbnail(file)
    print(time.time() - start, "Using Loop")

    start = time.time()
    with Pool(processes=4) as p:
        p.map(convert_to_thumbnail, files)
    print(time.time() - start, "Using Pool")

    start = time.time()
    p = Process(target=convert_to_thumbnail_process, args=(files, ))
    p.start()
    print(time.time() - start, "Using Process")

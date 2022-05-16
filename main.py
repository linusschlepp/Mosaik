import random
import time

from styles import *
from PIL import Image, ImageDraw
import sys
import pathlib
import PIL.ImageFile



try:
    file_name = sys.argv[3]
# mosaik_style = sys.argv[3]
    color_outer_mosaik = sys.argv[1]
    color_inner_mosaik = sys.argv[2]
except:
    pass

step = 50

if sys.argv[1] == "mosaikgrand":
    ultimate_style(step)

else:
    img = Image.new("RGB", (1250, 1250), color_outer_mosaik)

    draw = ImageDraw.Draw(img)
    w, h = img.size




    count = 0



    ran_num = random.randint(1,4)

    if(ran_num == 1):
        style_1(step, color_inner_mosaik, draw, count, w ,h)
    if(ran_num == 2):
        style_2(step, color_inner_mosaik, draw, count, w ,h)
    if (ran_num == 3):
        style_3(step, color_inner_mosaik, draw, count, w ,h)
    if (ran_num == 4):
        style_4(step, color_inner_mosaik, draw, count, w ,h)

    print(ran_num)

    print("Creating file")
    for x in range(5):
        print(".")
        time.sleep(0.20)


    img.save(file_name + ".png")
    print(file_name + ".png" + " was created")

import random
import time
import itertools
import threading
import sys
from styles import *
from PIL import Image, ImageDraw
import sys
import pathlib
import PIL.ImageFile

done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r')

def print_options():
    colors = ["red", "yellow", "cyan", "blue", "pink", "orange",
              "black", "white", "green", "purple", "grey", "violet", "ivory", "coral", "brown", "teal", "tan",
              "salmon", "lime", "gold", "aquamarine", "maroon", "orchid", "darkgrey", "darkgreen", "darkred",
              "darkblue"]


    print("Enter following commands: ")
    print("\t argv[0] = background color")
    print("\t argv[1] = color in the front")
    print("\t argv[2] = color in the front")
    print("\t Following colors are to your disposal: ")
    for color in colors:
        print("\t -"+ color)

    print("If you want to create a Mosaik, just enter: ")
    print("\t argv[0] = mosaikgrand")
    print("The colors are generated randomly, so you don't have to declare any!")




try:
    file_name = sys.argv[3]
    color_outer_mosaik = sys.argv[1]
    color_inner_mosaik = sys.argv[2]
except:
    pass

step = 50

if sys.argv[1] == "mosaikgrand":
    ultimate_style(step)
elif sys.argv[1] == "--help":
    print_options()


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


    print("Creating file... ")
    t = threading.Thread(target=animate)
    t.start()


    time.sleep(3)
    done = True



    img.save(file_name + ".png")
    print(file_name + ".png" + " was created")

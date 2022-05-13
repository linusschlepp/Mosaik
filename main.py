import random

from PIL import Image, ImageDraw
import sys
import pathlib
import PIL.ImageFile

file_name = sys.argv[3]
color_outer_mosaik = sys.argv[1]
color_inner_mosaik = sys.argv[2]

i = Image.new("RGB", (1250, 1250), color_outer_mosaik)

draw = ImageDraw.Draw(i)
w, h = i.size

step = 50

count = 0
for y in range(0, w, step):
    count = count +1
    for x in range(0, h, step):
        draw.polygon([(x,y) , (x,y+step), (x+step,y)], fill=color_inner_mosaik)

i.save(file_name + ".png")
print(sys.argv[1] + " " + sys.argv[2])
print(pathlib.Path(__file__).parent.resolve())

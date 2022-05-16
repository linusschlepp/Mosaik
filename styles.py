import random
from PIL import Image, ImageDraw
import cv2

def style_4(step, color_inner_mosaik, draw, count, w ,h):

    for y in range(0, w, step):
        count = count + 1
        pattern_1 = True
        for x in range(0, h, step):
            if count % 2:
                if pattern_1:
                    draw.polygon([(x, y), (x, y + step), (x+step, y)], fill=color_inner_mosaik)
                    pattern_1 = False
                else:
                    draw.polygon([(x , y ), (x+step, y + step), (x + step, y)], fill=color_inner_mosaik)
                    pattern_1 = True
            else:
                if pattern_1:
                    draw.polygon([(x , y+step ), (x+step, y + step), (x, y)], fill=color_inner_mosaik)
                    pattern_1 = False
                else:
                    draw.polygon([(x+step , y+step ), (x, y + step), (x + step, y)], fill=color_inner_mosaik)
                    pattern_1 = True


def ultimate_style(step):
    colors = ["red", "yellow", "cyan", "blue", "pink", "orange",
              "black", "white",  "green", "purple", "grey", "violet", "ivory", "coral", "brown", "teal", "tan",
              "salmon", "lime",  "gold", "aquamarine" ,  "maroon", "orchid", "darkgrey", "darkgreen"]



    for x in range(64):
        color_1 = colors[random.randint(0, len(colors) - 1)]
        color_2 = get_color_rec(colors, color_1)
        img = Image.new("RGB", (1250, 1250), color_1)

        draw = ImageDraw.Draw(img)
        w, h = img.size

        count = 0
        ran_num = random.randint(1,4)
        if (ran_num == 1):
            style_1(step, color_2, draw, count, w, h)
        if (ran_num == 2):
            style_2(step, color_2, draw, count, w, h)
        if (ran_num == 3):
            style_3(step, color_2, draw, count, w, h)
        if (ran_num == 4):
            style_4(step, color_2, draw, count, w, h)

        img.save("images/"+"pic"+ str(x) + ".png")
        print("pic"+ str(x) + ".png" + " was created")

        read_img = []

        for x in range(8):
            read_img.append(cv2.imread("images/"+"pic"+str(x)+".png"))

        im_v = cv2.vconcat(read_img)

        # show the output image
        cv2.save('sea_image.jpg', im_v)










def get_color_rec(colors, color_1):
    color_2 = colors[random.randint(0, len(colors)-1)]
    if color_2 != color_1:
        return color_2

    return get_color_rec(colors, color_1)






def style_1(step, color_inner_mosaik, draw, count, w ,h):

    for y in range(0, w, step):
        count = count + 1
        pattern_1 = True
        for x in range(0, h, step):
            if count % 2:
                if pattern_1:
                    draw.polygon([(x, y+step), (x+step, y + step), (x, y)], fill=color_inner_mosaik)
                    pattern_1 = False
                else:
                    draw.polygon([(x + step, y + step), (x, y + step), (x + step, y)], fill=color_inner_mosaik)
                    pattern_1 = True
            else:
                if pattern_1:
                    draw.polygon([(x , y ), (x, y + step), (x + step, y)], fill=color_inner_mosaik)
                    pattern_1 = False
                else:
                    draw.polygon([(x , y ), (x + step, y + step), (x + step, y)], fill=color_inner_mosaik)
                    pattern_1 = True


def style_2(step, color_inner_mosaik, draw, count, w ,h):
    for y in range(0, w, step):
        count = count + 1
        for x in range(0, h, step):
            if count % 2 == 0:
                draw.polygon([(x + step, y + step), (x, y + step), (x + step, y)], fill=color_inner_mosaik)
            else:
                draw.polygon([(x, y), (x, y + step), (x + step, y)], fill=color_inner_mosaik)



def style_3(step, color_inner_mosaik, draw, count, w ,h):
    for y in range(0, w, step):
        count = count + 1
        for x in range(0, h, step):
                draw.polygon([(x , y ), (x + step, y), (x, y+step)], fill=color_inner_mosaik)


def style_5(step, color_inner_mosaik, draw, count, w ,h):
    for y in range(0, w, step):
        count = count + 1
        for x in range(0, h, step):
                draw.polygon([(x , y ), (x + step, y), (x, y+step)], fill=color_inner_mosaik)
import random
from PIL import Image, ImageDraw
import cv2


def ultimate_style(step):
    colors = ["red", "yellow", "cyan", "blue", "pink", "orange",
              "black", "white", "green", "purple", "grey", "violet", "ivory", "coral", "brown", "teal", "tan",
              "salmon", "lime", "gold", "aquamarine", "maroon", "orchid", "darkgrey", "darkgreen", "darkred",
              "darkblue"]

    for x in range(36):
        # color_1 = colors[random.randint(0, len(colors) - 1)]
        color_1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # if color_1[0] < 127 or color_1[1] < 127 or color_1[2] < 127:
        #     color_2 = get_color_rec_spec(color_1, 127, 255)
        # elif color_1[0] > 127 or color_1[1] > 127 or color_1[2] > 127:
        #     color_2 = get_color_rec_spec(color_1, 0, 127)

        color_2 = get_color_rec(colors, color_1)
        img = Image.new("RGB", (1250, 1250), color_1)

        draw = ImageDraw.Draw(img)
        w, h = img.size

        count = 0
        ran_num = random.randint(1, 8)
        # if (ran_num == 1):
        #     style_1(step, color_2, draw, count, w, h)
        # if (ran_num == 2):
        #     style_2(step, color_2, draw, count, w, h)
        # if (ran_num == 3):
        #     style_3(step, color_2, draw, count, w, h)
        # if (ran_num == 4):
        #     style_4(step, color_2, draw, count, w, h)
        # if (ran_num == 5):
        #     style_5(step, color_2, draw, count, w, h)
        # if (ran_num == 6):
        #     style_6(step, color_2, draw, count, w, h)
        # if (ran_num == 7):
        #     style_7(step, color_2, draw, count, w, h)
        # if (ran_num == 8):
        #     style_8(step, color_2, draw, count, w, h)
        style_9(step, color_2, draw, count, w, h)

        img.save("images/" + "pic" + str(x) + ".png")
        print("pic" + str(x) + ".png" + " was created")
        print(ran_num)

    mosaiks = []
    count_1 = 0
    for y in range(6):
        read_img = []
        for x in range(6):
            read_img.append(cv2.imread("images/" + "pic" + str(count_1) + ".png"))
            count_1 = count_1 + 1
        im_v = cv2.vconcat(read_img)
        cv2.imwrite("mosaiks/mosaik" + str(y) + ".png", im_v)
        mosaiks.append(cv2.imread("mosaiks/mosaik" + str(y) + ".png"))

    im_h = cv2.hconcat(mosaiks)
    cv2.imwrite('finalmosaik.png', im_h)


def get_color_rec(colors, color_1):
    # color_2 = colors[random.randint(0, len(colors)-1)]
    color_2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if color_2 != color_1:
        return color_2

    return get_color_rec(colors, color_1)


# def get_color_rec_spec(color_1, start, end):
#     # color_2 = colors[random.randint(0, len(colors)-1)]
#     color_2 = (random.randint(start, end), random.randint(start, end), random.randint(start, end))
#     if color_2 != color_1:
#         return color_2
#
#     return get_color_rec_spec(color_1, start, end)


def style_1(step, color_inner_mosaik, draw, count, w, h):
    for y in range(0, w, step):
        count = count + 1
        pattern_1 = True
        for x in range(0, h, step):
            if count % 2 == 0:
                if pattern_1:
                    draw.polygon([(x, y + step), (x + step, y + step), (x, y)], fill=color_inner_mosaik)
                    pattern_1 = False
                else:
                    draw.polygon([(x + step, y + step), (x, y + step), (x + step, y)], fill=color_inner_mosaik)
                    pattern_1 = True
            else:
                if pattern_1:
                    draw.polygon([(x, y), (x, y + step), (x + step, y)], fill=color_inner_mosaik)
                    pattern_1 = False
                else:
                    draw.polygon([(x, y), (x + step, y + step), (x + step, y)], fill=color_inner_mosaik)
                    pattern_1 = True


def style_2(step, color_inner_mosaik, draw, count, w, h):
    for y in range(0, w, step):
        count = count + 1
        for x in range(0, h, step):
            if count % 2 == 0:
                draw.polygon([(x + step, y + step), (x, y + step), (x + step, y)], fill=color_inner_mosaik)
            else:
                draw.polygon([(x, y), (x, y + step), (x + step, y)], fill=color_inner_mosaik)


def style_3(step, color_inner_mosaik, draw, count, w, h):
    for y in range(0, w, step):
        count = count + 1
        for x in range(0, h, step):
            draw.polygon([(x, y), (x + step, y), (x, y + step)], fill=color_inner_mosaik)


def style_4(step, color_inner_mosaik, draw, count, w, h):
    for y in range(0, w, step):
        count = count + 1
        for x in range(0, h, step):
            if count % 2 == 0:
                draw.polygon([(x + step, y + step), (x, y + step), (x + step, y)], fill=color_inner_mosaik)
            else:
                draw.polygon([(x, y), (x + step, y + step), (x + step, y)], fill=color_inner_mosaik)


def style_5(step, color_inner_mosaik, draw, count, w, h):
    for y in range(0, w, step):
        count = count + 1
        pattern_1 = True
        for x in range(0, h, step):
            if count % 2 == 0:
                if pattern_1:
                    pattern_1 = False
                else:
                    draw.polygon([(x, y + step), (x + step, y + step), (x, y)], fill=color_inner_mosaik)
                    pattern_1 = True
            else:
                draw.polygon([(x, y), (x + step, y + step), (x + step, y)], fill=color_inner_mosaik)


def style_6(step, color_inner_mosaik, draw, count, w, h):
    for y in range(0, w, step):
        count = count + 1
        pattern_1 = True
        for x in range(0, h, step):
            if count % 2 == 0:
                if pattern_1:
                    draw.polygon([(x, y + step), (x + step, y + step), (x, y)], fill=color_inner_mosaik)
                    pattern_1 = False
                else:
                    draw.polygon([(x + step, y + step), (x, y + step), (x + step, y)], fill=color_inner_mosaik)
                    pattern_1 = True
            else:
                if pattern_1:
                    draw.polygon([(x, y), (x + step, y + step), (x + step, y)], fill=color_inner_mosaik)
                    pattern_1 = False
                else:
                    draw.polygon([(x, y), (x, y + step), (x + step, y)], fill=color_inner_mosaik)
                    pattern_1 = True


def style_7(step, color_inner_mosaik, draw, count, w, h):
    for y in range(0, w, step):
        count = count + 1
        pattern_1 = True
        for x in range(0, h, step):
            if count % 2 == 0:
                if pattern_1:
                    draw.polygon([(x, y), (x + step, y + step), (x + step, y)], fill=color_inner_mosaik)
                    pattern_1 = False
                else:
                    draw.polygon([(x, y), (x, y + step), (x + step, y)], fill=color_inner_mosaik)
                    pattern_1 = True
            else:
                if pattern_1:
                    draw.polygon([(x, y), (x + step, y + step), (x + step, y)], fill=color_inner_mosaik)
                    pattern_1 = False
                else:
                    draw.polygon([(x, y), (x, y + step), (x + step, y)], fill=color_inner_mosaik)
                    pattern_1 = True


def style_8(step, color_inner_mosaik, draw, count, w, h):
    for y in range(0, w, step):
        count = count + 1
        pattern_1 = True
        inner_count = 0
        switch = True
        for x in range(0, h, step):
            if inner_count == 2:
                inner_count=0
                switch = not switch
            if count % 2 == 0:
                if switch:
                    if pattern_1:
                        draw.polygon([(x + step, y + step), (x, y + step), (x + step, y)], fill=color_inner_mosaik)
                        pattern_1 = False
                    else:
                        draw.polygon([(x, y + step), (x + step, y + step), (x, y)], fill=color_inner_mosaik)
                        pattern_1 = True
                else:
                    if pattern_1:
                        draw.polygon([(x, y + step), (x + step, y + step), (x, y)], fill=color_inner_mosaik)
                        pattern_1 = False
                    else:
                        draw.polygon([(x + step, y + step), (x, y + step), (x + step, y)], fill=color_inner_mosaik)
                        pattern_1 = True
            else:

                if switch:
                    if pattern_1:
                        draw.polygon([(x, y+step), (x + step, y + step), (x, y)], fill=color_inner_mosaik)
                        pattern_1 = False
                    else:
                        draw.polygon([(x+step, y+step), (x, y + step), (x + step, y)], fill=color_inner_mosaik)
                        pattern_1 = True
                else:
                    if pattern_1:
                        draw.polygon([(x + step, y + step), (x, y + step), (x + step, y)], fill=color_inner_mosaik)
                        pattern_1 = False
                    else:
                        draw.polygon([(x, y + step), (x + step, y + step), (x, y)], fill=color_inner_mosaik)
                        pattern_1 = True



def style_9(step, color_inner_mosaik, draw, count, w, h):
    for y in range(0, w, step):
        for x in range(0, h, step):
            ran_num = random.randint(1,4)

            if ran_num == 1:
                draw.polygon([(x + step, y + step), (x, y + step), (x + step, y)], fill=color_inner_mosaik)
            if ran_num == 2:
                draw.polygon([(x, y + step), (x + step, y + step), (x, y)], fill=color_inner_mosaik)
            if ran_num == 3:
                draw.polygon([(x,y ), (x, y + step), (x+step, y)], fill=color_inner_mosaik)
            if ran_num == 4:
                draw.polygon([(x, y), (x+step, y + step), (x + step, y)], fill=color_inner_mosaik)





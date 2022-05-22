import random
from PIL import Image, ImageDraw
import cv2


def ultimate_style(step):

    for x in range(36):

        color_1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


        color_2 = get_color_rec(color_1)
        img = Image.new("RGB", (1250, 1250), color_1)

        draw = ImageDraw.Draw(img)
        w, h = img.size

        count = 0
        ran_num = random.randint(1, 8)

        mosaik_style(step, color_2, draw, count, w, h)

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


def get_color_rec(color_1):
    color_2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if color_2 != color_1:
        return color_2

    return get_color_rec(color_1)



def mosaik_style(step, color_inner_mosaik, draw,  w, h):
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






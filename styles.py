

def style_1(step, color_inner_mosaik, draw, count, w ,h):
    for y in range(0, w, step):
        if count == 3:
            count = 0
        count = count +1
        for x in range(0, h, step):
            if count == 2:
                draw.polygon([(x+step, y+step), (x, y + step), (x + step, y)], fill=color_inner_mosaik)
            elif count == 3:
                draw.polygon([(x+step, y), (x, y), (x + step, y+step)], fill=color_inner_mosaik)
            else:
                draw.polygon([(x,y) , (x,y+step), (x+step,y)], fill=color_inner_mosaik)


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
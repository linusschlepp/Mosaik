


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





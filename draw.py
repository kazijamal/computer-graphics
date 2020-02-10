from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x = int(x0)
    y = int(y0)
    a = y1 - y0
    b = (x1 - x0) * -1
    if b == 0:
        if y1 > y0:
            while y <= y1:
                plot(screen, color, x, y)
                y += 1
        else:
            while y1 <= y:
                plot(screen, color, x, y)
                y -= 1
    else:
        m = a / (-1 * b)
        d = 2 * a + b
        if 0 <= m and m <= 1:
            if x0 < x1:
                while x <= x1:
                    plot(screen, color, x, y)
                    if d > 0:
                        y += 1
                        d += 2 * b
                    x += 1
                    d += 2 * a
            else:
                d = -2 * a - b
                while x > x1:
                    plot(screen, color, x, y)
                    if d > 0:
                        y -= 1
                        d -= 2 * b
                    x -= 1
                    d -= 2 * a
        elif m > 1:
            if x0 < x1:
                d = 2 * b + a
                while y <= y1:
                    plot(screen, color, x, y)
                    if d < 0:
                        x += 1
                        d += 2 * a
                    y += 1
                    d += 2 * b
            else:
                d = -2 * b + -1 * a
                while y > y1:
                    plot(screen, color, x, y)
                    if d < 0:
                        x -= 1
                        d -= 2 * a
                    y -= 1
                    d -= 2 * b
        elif m < -1:
            if y0 < y1:
                d = -1 * a + 2 * b
                while y <= y1:
                    plot(screen, color, x, y)
                    if d > 0:
                        x -= 1
                        d -= 2 * a
                    y += 1
                    d += 2 * b
            else:
                d = a - 2 * b
                while y > y1:
                    plot(screen, color, x, y)
                    if d > 0:
                        x += 1
                        d += 2 * a
                    y -= 1
                    d -= 2 * b
        elif m >= -1:
            if x0 > x1:
                d = -2 * a + b
                while x > x1:
                    plot(screen, color, x, y)
                    if d < 0:
                        y += 1
                        d += 2 * b
                    x -= 1
                    d -= 2 * a
            else:
                d = 2 * a - b
                while x <= x1:
                    plot(screen, color, x, y)
                    if d < 0:
                        y -= 1
                        d -= 2 * b
                    x += 1
                    d += 2 * a
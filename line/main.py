from display import *
from draw import *

s = new_screen()

# red lines
c = [ 100, 0, 0 ]
x = 125
while x < XRES - 101:
    if x % 20 == 0:
        draw_line(x, YRES-101, x, 101, s, c)
    x += 1

y = 125
while y < YRES - 101:
    if y % 20 == 0:
        draw_line(XRES-101, y, 101, y, s, c)
    y += 1

# green lines
c = [ 0, 255, 0 ]

# dollar bill outline
draw_line(100, 100, XRES-100, 100, s, c)
draw_line(100, YRES-100, XRES-100, YRES-100, s, c)
draw_line(100, 100, 100, YRES-100, s, c)
draw_line(XRES-100, YRES-100, XRES-100, 100, s, c)

# triangle
draw_line(XRES/2 + 125, 150, XRES/2 - 125, 150, s, c)
draw_line(XRES/2 + 125, 150, XRES/2, YRES-150, s, c)
draw_line(XRES/2 - 125, 150, XRES/2, YRES-150, s, c)

# eye
draw_line(XRES/2, YRES/2 + 10, XRES/2 + 25, YRES/2, s, c)
draw_line(XRES/2, YRES/2 + 10, XRES/2 -25, YRES/2, s, c)
draw_line(XRES/2, YRES/2 - 10, XRES/2 + 25, YRES/2, s, c)
draw_line(XRES/2, YRES/2 - 10, XRES/2 -25, YRES/2, s, c)

# bricks
y = 150
x1 = XRES/2 - 125
x2 = XRES/2 + 125
while y < YRES - 150:
    if y % 10 == 0:
        draw_line(x1, y, x2, y, s, c)
    y += 1
    x1 += 0.63
    x2 -= 0.63

# 1
x = 125
while x < 150:
    if x % 4 == 0:
        draw_line(x, YRES-125, x, YRES-200, s, c)
        draw_line(x, 125, x, 200, s, c)
    x += 1

x = XRES-125
while x > XRES-150:
    if x % 4 == 0:
        draw_line(x, YRES-125, x, YRES-200, s, c)
        draw_line(x, 125, x, 200, s, c)
    x -= 1

# eyes
draw_line(XRES/4, YRES/2 + 50, XRES/4 + 50, YRES/2, s, c)
draw_line(XRES/4, YRES/2 + 50, XRES/4 - 50, YRES/2, s, c)
draw_line(XRES/4, YRES/2 - 50, XRES/4 + 50, YRES/2, s, c)
draw_line(XRES/4, YRES/2 - 50, XRES/4 - 50, YRES/2, s, c)

draw_line((XRES-XRES/4), YRES/2 + 50, (XRES-XRES/4) + 50, YRES/2, s, c)
draw_line((XRES-XRES/4), YRES/2 + 50, (XRES-XRES/4) - 50, YRES/2, s, c)
draw_line((XRES-XRES/4), YRES/2 - 50, (XRES-XRES/4) + 50, YRES/2, s, c)
draw_line((XRES-XRES/4), YRES/2 - 50, (XRES-XRES/4) - 50, YRES/2, s, c)

# red lines
c = [ 255, 0, 0 ]
draw_line(XRES-101, YRES-101, 99, 99, s, c)
draw_line(99, YRES-101, XRES-101, 99, s, c)
draw_line(XRES/2, YRES-101, XRES/2, 99, s, c)
draw_line(XRES-101, YRES/2, 99, YRES/2, s, c)
draw_line(XRES/4, YRES-101, 3*XRES/4, 99, s, c)
draw_line(XRES/4, 99, 3*XRES/4, YRES-101, s, c)

# #octants 1 and 5
# draw_line(0, 0, XRES-1, YRES-1, s, c)
# draw_line(0, 0, XRES-1, YRES / 2, s, c) 
# draw_line(XRES-1, YRES-1, 0, YRES / 2, s, c)

# #octants 8 and 4
# c[BLUE] = 255
# draw_line(0, YRES-1, XRES-1, 0, s, c)  
# draw_line(0, YRES-1, XRES-1, YRES/2, s, c)
# draw_line(XRES-1, 0, 0, YRES/2, s, c)
    
# #octants 2 and 6
# c[RED] = 255
# c[GREEN] = 0
# c[BLUE] = 0
# draw_line(0, 0, XRES/2, YRES-1, s, c)
# draw_line(XRES-1, YRES-1, XRES/2, 0, s, c)

# #octants 7 and 3
# c[BLUE] = 255
# draw_line(0, YRES-1, XRES/2, 0, s, c)
# draw_line(XRES-1, 0, XRES/2, YRES-1, s, c)

# #horizontal and vertical
# c[BLUE] = 0
# c[GREEN] = 255
# draw_line(0, YRES/2, XRES-1, YRES/2, s, c)
# draw_line(XRES/2, 0, XRES/2, YRES-1, s, c)


display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')

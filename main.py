from display import *
from draw import *
from matrix import *

screen = new_screen()

x1 = 250
y1 = 0
x2 = 350
y2 = 250

matrix = new_matrix()
color = [119, 255, 131]

while x2 > 300:
    add_edge(matrix, x1, y1, 0, x2, y2, 0)
    x2 -= 1

draw_lines(matrix, screen, color)

matrix = new_matrix()
color = [94, 234, 3]

while x2 > 200:
    add_edge(matrix, x1, y1, 0, x2, y2, 0)
    x2 -= 1

draw_lines(matrix, screen, color)

matrix = new_matrix()
color = [53, 186, 41]

while x2 > 150:
    add_edge(matrix, x1, y1, 0, x2, y2, 0)
    x2 -= 1

draw_lines(matrix, screen, color)

x1 = 250
y1 = 500
x2 = 350
y2 = 250

matrix = new_matrix()
color = [94, 234, 3]

while x2 > 300:
    add_edge(matrix, x1, y1, 0, x2, y2, 0)
    x2 -= 1

draw_lines(matrix, screen, color)

matrix = new_matrix()
color = [53, 186, 41]

while x2 > 200:
    add_edge(matrix, x1, y1, 0, x2, y2, 0)
    x2 -= 1

draw_lines(matrix, screen, color)

matrix = new_matrix()
color = [119, 255, 131]

while x2 > 150:
    add_edge(matrix, x1, y1, 0, x2, y2, 0)
    x2 -= 1

draw_lines(matrix, screen, color)

display(screen)

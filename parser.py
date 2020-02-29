from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""


def parse_file(fname, points, transform, screen, color):
    f = open(fname, 'r')
    lines = f.read().split('\n')
    n = 0
    while n < len(lines) and lines[n] != 'quit':
        cmd = lines[n]
        if cmd == 'line':
            args = lines[n+1]
            coords = [int(arg) for arg in args.split(' ')]
            add_edge(points, coords[0], coords[1], coords[2],
                     coords[3], coords[4], coords[5])
            n += 2
        elif cmd == 'ident':
            ident(transform)
            n += 1
        elif cmd == 'scale':
            args = lines[n+1]
            scalefactor = [int(arg) for arg in args.split(' ')]
            scale = make_scale(scalefactor[0], scalefactor[1], scalefactor[2])
            matrix_mult(scale, transform)
            n += 2
        elif cmd == 'move':
            args = lines[n+1]
            translation = [int(arg) for arg in args.split(' ')]
            translate = make_translate(
                translation[0], translation[1], translation[2])
            matrix_mult(translate, transform)
            n += 2
        elif cmd == 'rotate':
            args = lines[n+1]
            arguments = args.split(' ')
            axis = arguments[0]
            theta = float(arguments[1])
            if axis == 'x':
                rotate = make_rotX(theta)
            elif axis == 'y':
                rotate = make_rotY(theta)
            elif axis == 'z':
                rotate = make_rotZ(theta)
            matrix_mult(rotate, transform)
            n += 2
        elif cmd == 'apply':
            matrix_mult(transform, points)
            n += 1
        elif cmd == 'display':
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
            n += 1
        elif cmd == 'save':
            args = lines[n+1]
            clear_screen(screen)
            draw_lines(points, screen, color)
            filename = args
            save_extension(screen, filename)
            n += 2

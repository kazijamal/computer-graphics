from display import *
from draw import *
from parser import *
from matrix import *
from makescript import *
import math

screen = new_screen()
color = [255, 0, 0]
edges = []
transform = new_matrix()

# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )

make_script('myscript')

parse_file('script', edges, transform, screen, color)
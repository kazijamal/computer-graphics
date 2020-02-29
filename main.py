from display import *
from draw import *
from parser import *
from matrix import *
from makescript import *

screen = new_screen()
color = [199, 149, 31]

edges = new_matrix(0,0)
transform = new_matrix()
ident(transform)

make_script('myscript')

parse_file('myscript', edges, transform, screen, color)

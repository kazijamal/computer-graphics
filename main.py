from display import *
from draw import *
from parser import *
from matrix import *
from makescript import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

make_script('myscript')
parse_file( 'thefacestrikesback', edges, transform, screen, color )

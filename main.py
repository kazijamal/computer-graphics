from display import *
from draw import *
from parser import *
from matrix import *
import math


# lighting values
view = [0,
        0,
        1]
ambient = [50,
           50,
           50]
light = [[0.5,
          0.75,
          1],
         [255,
          255,
          0]]
areflect = [0.1,
            0.1,
            0.1]
dreflect = [0.5,
            0.5,
            0.5]
sreflect = [0.5,
            0.5,
            0.5]


screen = new_screen()
zbuffer = new_zbuffer()
color = [255, 255, 0]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [t]


parse_file('script', edges, polygons, csystems, screen, zbuffer,
           color, view, ambient, light, areflect, dreflect, sreflect)

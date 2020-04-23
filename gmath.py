import math
from display import *

# IMPORANT NOTE

# Ambient light is represeneted by a color value

# Point light sources are 2D arrays of doubles.
#      - The fist index (LOCATION) represents the vector to the light.
#      - The second index (COLOR) represents the color.

# Reflection constants (ka, kd, ks) are represened as arrays of
# doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

# lighting functions


def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect):
    lambient = calculate_ambient(ambient, areflect)
    ldiffuse = calculate_diffuse(light, dreflect, normal)
    lspecular = calculate_specular(light, sreflect, view, normal)
    return [lambient[0] + ldiffuse[0] + lspecular[0], lambient[1] + ldiffuse[1] + lspecular[1], lambient[2] + ldiffuse[2] + lspecular[2]]


def calculate_ambient(alight, areflect):
    l_r = alight[0] * areflect[0]
    l_g = alight[1] * areflect[1]
    l_b = alight[2] * areflect[2]
    return [limit_color(l_r), limit_color(l_g), limit_color(l_b)]


def calculate_diffuse(light, dreflect, normal):
    normalize(normal)
    normalize(light[LOCATION])
    d_p = dot_product(normal, light[LOCATION])
    l_r = light[COLOR][0] * dreflect[0] * d_p
    l_g = light[COLOR][1] * dreflect[1] * d_p
    l_b = light[COLOR][2] * dreflect[2] * d_p
    return [limit_color(l_r), limit_color(l_g), limit_color(l_b)]


def calculate_specular(light, sreflect, view, normal):
    normalize(normal)
    normalize(light[LOCATION])
    d_p = dot_product(normal, light[LOCATION])
    t = [normal[0] * d_p, normal[1] * d_p, normal[2] * d_p]
    s = [t[0] - light[LOCATION][0], t[1] - light[LOCATION][1], t[2] - light[LOCATION][2]]
    r = [t[0] + s[0], t[1] + s[1], t[2] + s[2]]
    d_p = dot_product(r, view)
    l_r = light[COLOR][0] * (sreflect[0] * d_p)**2
    l_g = light[COLOR][1] * (sreflect[1] * d_p)**2
    l_b = light[COLOR][2] * (sreflect[2] * d_p)**2
    return [limit_color(l_r), limit_color(l_g), limit_color(l_b)]


def limit_color(color):
    if color > 255:
        return 255
    elif color < 0:
        return 0
    return int(color)

# vector functions
# normalize vetor, should modify the parameter


def normalize(vector):
    magnitude = math.sqrt(vector[0] * vector[0] +
                          vector[1] * vector[1] +
                          vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

# Return the dot porduct of a . b


def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

# Calculate the surface normal for the triangle whose first
# point is located at index i in polygons


def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N

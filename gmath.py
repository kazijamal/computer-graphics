import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    pass

#Return the dot porduct of a . b
def dot_product(a, b):
    i = 0
    ans = 0
    while i < 3:
        ans += a[i] * b[i]
        i += 1
    return ans

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    return None

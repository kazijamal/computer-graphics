import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    pass

#Return the dot porduct of a . b
def dot_product(a, b):
    ans = 0
    for i in range(0,3):
        ans += a[i] * b[i]
    return ans

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    p0 = polygons[i]
    p1 = polygons[i+1]
    p2 = polygons[i+2]
    a = [p1[0]-p0[0], p1[1]-p0[1], p1[2]-p0[2]]
    b = [p2[0]-p0[0], p2[1]-p0[1], p2[2]-p0[2]]
    ans = [0, 0, 0]
    ans[0] = a[1]*b[2] - a[2]*b[1]
    ans[1] = a[2]*b[0] - a[0]*b[2]
    ans[2] = a[0]*b[1] - a[1]*b[2]
    return ans

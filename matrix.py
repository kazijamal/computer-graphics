"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

# print the matrix such that it looks like
# the template in the top comment


def print_matrix(matrix):
    for r in range(len(matrix[0])):
        for c in range(len(matrix)):
            print(matrix[c][r], ' ', end='')
        print()
    print()

# turn the paramter matrix into an identity matrix
# you may assume matrix is square


def ident(matrix):
    i = 0
    for r in range(len(matrix[0])):
        counter = 0
        for c in range(len(matrix)):
            if counter != i:
                matrix[c][r] = 0
            else:
                matrix[c][r] = 1
            counter += 1
        i += 1

# multiply m1 by m2, modifying m2 to be the product
# m1 * m2 -> m2

# THIS METHOD OVERWRITES COLUMNS WHICH MODIFIES THE NEXT DOT PRODUCT
# def matrix_mult(m1, m2):
#     for r in range(len(m1[0])):
#         for c in range(len(m2)):
#             ans = 0
#             for i in range(len(m1[0])):
#                 ans += m1[i][r] * m2[c][i]
#             m2[c][r] = ans

# THIS METHOD CREATES AN ADDITIONAL METHOD


def matrix_mult(m1, m2):
    product = new_matrix(len(m1[0]), len(m2))
    for r in range(len(m1[0])):
        for c in range(len(m2)):
            ans = 0
            for i in range(len(m1[0])):
                ans += m1[i][r] * m2[c][i]
            product[c][r] = ans
    for r in range(len(product[0])):
        for c in range(len(product)):
            m2[c][r] = product[c][r]

# THIS METHOD CREATES TEMPORARY COLUMNS
# def matrix_mult(m1, m2):
#     for r in range(len(m1[0])):
#         temp_column = [0, 0, 0, 0]
#         for c in range(len(m2)):
#             ans = 0
#             for i in range(len(m1[0])):
#                 ans += m1[i][r] * m2[c][i]
#             temp_column[r] = ans
#         m2[r] = temp_column


def new_matrix(rows=4, cols=4):
    m = []
    for c in range(cols):
        m.append([])
        for r in range(rows):
            m[c].append(0)
    return m


# testing
# m1 = new_matrix()
# print_matrix(m1)
# ident(m1)
# print_matrix(m1)

# m2 = new_matrix(4, 8)
# m2[0][0] = 3
# print_matrix(m2)
# matrix_mult(m1, m2)
# print_matrix(m2)

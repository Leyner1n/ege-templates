from itertools import *


# def f(x, y, z, w):
#     return ((x <= y) == (z <= w)) or (x and w)
#
#
# for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
#     table = [(1, a1, a2, a3), (1, 1, a4, a5), (1, 1, 1, a6)]
#     if len(table) == len(set(table)):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
#                 print(p)
#
#
# def f(x, y, z, w):
#     return ((x == (not(y))) <= (y and (not(z)))) or (z and (not(w)))
#
#
# for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
#     table = [(0, 0, a1, 0), (a2, 0, a3, 0), (a4, a5, a6, 0)]
#     if len(table) == len(set(table)):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
#                 print(p)




# def f(a, b, c, d):
#     return c and (a or d) and (d <= b)
#
<<<<<<< HEAD
=======
# print(c)


# a = '0123456789'
# c = 0 
>>>>>>> 51fb2cf63c36bc5c473a552d8b6b8626687cd30b
#
# for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
#     table = [(a1, a2, a3, 0), (a4, 1, 0, a5), (0, a6, 1, 0)]
#     if len(table) == len(set(table)):
#         for p in permutations('abcd'):
#             if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
#                 print(p)


# def f(w, x, y):
#     return (x <= y) and (w or (not w))
#
#
# for a1, a2, a3 in product([0, 1], repeat=3):
#     table = [(1, 1, 0), (a1, 1, a2), (1, 0, 1), (1, a3, 1)]
#     if len(table) == len(set(table)):
#         for p in permutations('wxy'):
#             if [f(**dict(zip(p, r))) for r in table] == [0, 0, 1, 1]:
#                 print(p)





























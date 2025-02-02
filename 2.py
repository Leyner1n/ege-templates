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


# a = 'ВЛТУ'
# c = 1
# for a1, a2, a3, a4 in product(a, repeat=4):
#     word = a1 + a2 + a3 + a4
#     print(c, word)
#     c += 1

# a = 'ЖИРАФ'
# c = 0
# for a1, a2, a3, a4 in product(a, repeat=4):
#     word = a1 + a2 + a3 + a4
#     if word.count('Р') == 1:
#         c += 1
#
# print(c)


# a = '0123456789'
# c = 0
#
# for a1, a2, a3, a4, a5 in product(a, repeat=5):
#     word1 = a1 + a2 + a3 + a4 + a5
#     word2 = ''
#     if word1.count('3') == 2:
#         for w in word1:
#             if int(w) % 2 != 0:
#                 word2 += 'x'
#             else:
#                 word2 += w
#         if not('x2' in word2 or '2x' in word2):
#             c += 1
#             print(f'{c}: {word2}')


# c = 1
#
# for a1, a2, a3, a4, a5, a6 in product('БКФ', repeat=6):
#     w = a1 + a2 + a3 + a4 + a5 + a6
#     print(c, w)
#     c += 1


# a = '0234567'
# c = 0
#
# for i in permutations(a, 5):
#     x = ''.join(i)
#     if x[0] != '0':
#         x = x.replace('7', '1').replace('5', '1').replace('3', '1').replace('6', '0').replace('4', '0').replace('2',                                                                                     '0')
#         if ('00' not in x) and ('11' not in x):
#             c += 1
#
# print(c)

# s = 101 * '1'
#
# while '111' in s:
#     s = s.replace('111', '22', 1).replace('222', '11', 1)
#
# print(s)


# s = '4' + 125 * '6' + '4'
#
# while '63' in s or '664' in s or '6665' in s:
#     if '63' in s:
#         s = s.replace('63', '4', 1)
#     else:
#         if '664' in s:
#             s = s.replace('664', '5', 1)
#         else:
#             if '6665' in s:
#                 s = s.replace('6665', '3', 1)
#
# print(s)


# m = set()
#
# for i in range(2, 1000):
#     s = i * '8'
#
#     while '555' in s or '888' in s:
#         s = s.replace('555', '8', 1).replace('888', '55', 1)
#     m.add(s)
#
# print(len(m))



# s = 200 * '5'
# while '555' in s or '333' in s:
#     if '555' in s:
#         s = s.replace('555', '3', 1)
#     else:
#         s = s.replace('333', '5', 1)
#
# print(sum([int(i) for i in s]))

from itertools import *
from functools import *
from turtle import *

# 2
# def f(w, x, y, z):
#     return (x and (z <= w) and (not y))
#
#
# for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
#     table = [(a1, a2, 1, a3), (a4, 1, 0, a5), (1, 0, a6, a7)]
#     for p in permutations('wxyz'):
#         if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
#             print(p)  # xwzy


# 5
# lst = []
# for n in range(1, 10_000):
#     r = f'{n:b}'
#     if sum([int(c) for c in r]) % 2 == 0:
#         r = '10' + r[2:] + '0'
#     else:
#         r = '11' + r[2:] + '1'
#     if int(r, 2) > 480:
#         lst.append((n, r, int(r, 2)))
#
# print(min(lst))  # 176


# 6
# tracer(0)
# k = 100
# screensize(20_000, 20_000)
# left(90)
# pd()
#
# right(30)
# for i in range(3):
#     right(150)
#     forward(6 * k)
#     right(30)
#     forward(12 * k)
# pu()
#
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         setpos(x * k, y * k)
#         dot(3)
#
# done()  # 30


# 8
# lst = []
# gl = 'ИАЭ'
# sogl = 'ДГШ'
# for p in product('ДГИАШЭ', repeat=5):
#     s = ''.join(p)
#     if (s[0] not in gl) and (s[-1] not in sogl):
#         lst.append(s)
#
# print(len(lst))


# 9
# file = open('./txt/9-12-04.txt').read()
#
# counter = 0
# for f in file.split('\n'):
#     s = [int(i) for i in f.split()]
#     if len(s):
#         a1 = [i for i in s if s.count(i) == 3]
#         if len(set(a1)) == 2:
#             a2 = [i for i in s if s.count(i) == 1]
#             # print(s, a1, a2, set(a1))
#             # print(max(set(a1)), a2[0])
#             if max(set(a1)) > a2[0]:
#                 counter += 1
#
# print(counter)  # 1


# 12
# def f(s):
#     while ('31' in s) or ('211' in s) or ('1111' in s):
#         if '31' in s:
#             s = s.replace('31', '1', 1)
#         if '211' in s:
#             s = s.replace('211', '13', 1)
#         if '1111' in s:
#             s = s.replace('1111', '2', 1)
#     return s
#
# char = '3'
# for n in range(3, 10_000):
#     F = f(char + (n * '1'))
#     if sum([int(i) for i in F]) == 15:
#         print(n, F)  # 50
#         break


# 14
# alphabet = '01234567889ABCDEFGHIJK'
# for x in alphabet:
#     s = int(f'82934{x}2', 21) + int(f'2924{x}{x}7', 21) + int(f'67564{x}8', 21)
#     if s % 20 == 0:
#         print(x, s // 20)
#         break

# 15
# @lru_cache(None)
# def f(n):
#     if n <= 5:
#         return 1
#     return n + f(n - 2)
#
#
# for i in range(1, 2500):
#     f(i)
#
# print(f(2126) - f(2122))  # 4250


# 17
# file = open('./txt/17-12-04.txt').read()
# f = [int(i) for i in file.split()]
# answer1 = sum(i for i in f if i < 0)
# count = 0
# lst = []
#
# for i in range(len(f) - 3):
#     answer2 = sorted([f[i], f[i+1], f[i+2]])
#     if (answer2[0] * answer2[-1]) > answer1:
#         count += 1
#         lst.append(sum(answer2))
#
# print(count, min(lst))  # 10006 28854


# 19-21
# def f(s, m):
#     if s <= 87:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#
#     h = [f(s - 2, m - 1), f(s // 2, m - 1)]
#
#     return any(h) if m % 2 != 0 else all(h)
#
#
# print('19', [s for s in range(89, 1000) if not f(s, 1) and f(s, 2)])  # 176
# print('21', [s for s in range(89, 1000) if not f(s, 1) and f(s, 3)])  # 178 179
# print('22', [s for s in range(89, 1000) if not f(s, 2) and f(s, 4)])  # 180



























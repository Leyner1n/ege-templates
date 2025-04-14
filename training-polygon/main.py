from itertools import *
from turtle import *
from functools import *
from sys import *


# def f(n):
#     ch = ''
#     while n > 0:
#         ch += str(n % 4)
#         n //= 4
#     return ch[::-1]
#
#
# for n in range(10_000, 1, -1):
#     r = f(n)
#     if n % 4 == 0:
#         r = '2' + r + '03'
#     else:
#         r = r + f'{f(n % 4 * 5)}'
#     r = int(r, 4)
#     if r <= 567:
#         print(n, r)


# tracer(0)
# k = 19
# left(90)
# screensize(10_000, 10_000)
#
# pd()
# forward(25 * k)
# right(45)
# forward(50 * k)
# pu()
#
# forward(-50 * k)
# right(45)
# forward(15 * k)
# left(90)
# forward(30 * k)
#
# pd()
#
# right(180)
# forward(60 * k)
# forward(-5 * k)
# right(90)
# forward(31 * k)
#
# pu()
#
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         setpos(x * k, y * k)
#         dot(5)
#
# done()

# lst = []
# for p in product('1234567890', repeat=6):
#     s = ''.join(p)
#     total = bin(int(s))[2:]
#     if total.count('0') == 19:
#         lst.append(total)
#
# print(len(lst))


# for n in range(10, 10_000):
#     r = bin(n)[2:]
#
#     if n % 5 == 0:
#         r = r[2:] + r
#     else:
#         r = r + bin((n % 5) * 5)[2:]
#
#     if n % 2 != 0 and int(r, 2) < 312:
#         print(n, r, int(r, 2))  # 35


# tracer(0)
# left(90)
# k = 20
# pd()
# for _ in range(2):
#     forward(11 * k)
#     right(90)
#     forward(17 * k)
#     right(90)
# pu()
# forward(7 * k)
# left(90)
# forward(-1 * k)
# right(90)
# pd()
# for _ in range(2):
#     forward(15 * k)
#     right(90)
#     forward(7 * k)
#     right(90)
# pu()
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         setpos(x * k, y * k)
#         dot(5)
#
# done()  40


# txt = open('./txt/9-08-04.txt').read()
#
# counter = 0
# for t in txt.split('\n'):
#     l1 = sorted([int(i) for i in t.split()])
#     ch = [i for i in l1 if i % 2 == 0]
#     nch = [i for i in l1 if i % 2 != 0]
#     if len(l1):
#         if l1[3] < (l1[0] + l1[1] + l1[2]):
#             if sum(ch) == sum(nch):
#                 counter += 1
#
# print(counter)  # 13


# lst = []
# for x in range(10_000, 1, -1):
#     n = (12 * x * 734) ** 24 + (8 * x * 95 * x * 3) ** 24 + (24 * x * 796) ** 24
#     if n % 23 == 0:
#         t = n // 23
#         print(x, t)
#         print(int(str(t), 24))
#         break


# @lru_cache(None)
# def f(n):
#     if n < 5:
#         return 4 ** 4
#     return 4 * f(n - 4) + 4
#
#
# for i in range(1, 10_000):
#     f(i)
#
#
# print(f(4048)/f(4036))  # 64


# file = open('./txt/17-08-04.txt')
#
# f = [int(i) for i in file]
# dv = [i for i in f if len(str(i)) == 2]
# sum_lst = []
# count = 0
#
#
# for i in range(len(f) - 2):
#     answer1 = (int(str(f[i])[-1]) + int(str(f[i + 1])[-1]))
#     if answer1 == 4:
#         count += 1
#         answer2 = int(str(f[i])) + int(str(f[i + 1]))
#         sum_lst.append(answer2)
#
# print(count, min(sum_lst))  # 243 3614


# sogl = 'ЛСТР'
# counter = 0
# for p in product('ЛЮСТРА', repeat=5):
#     s = ''.join(p)
#     if s.count('Ю') <= 2:
#         print(s)
#         if s[-1] not in sogl:
#             counter += 1
#
# print(counter)  # 2400


# def f(w, x, y, z):
#     return (y and (x or z) or (not (y or z)) or w)
#
#
# for a1, a2, a3, a4 in product([0, 1], repeat=4):
#     table = [(1, a1, 0, 1), (a2, 1, 0, a3), (0, 0, a4, 1)]
#     if len(table) == len(set(table)):
#         for p in permutations('wxyz'):
#             if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
#                 print(p)  # xywz


# s = 111 * '3'
#
# while '33333' in s or '1111' in s:
#     if '33333' in s:
#         s = s.replace('33333', '111', 1)
#     else:
#         s = s.replace('111', '33', 1)
#
# print(s)
# print(sum([int(i) for i in s]))


# def f(s, m):
#     if s <= 17:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#
#     h = [f(s - 3, m - 1), f(s - 5, m - 1), f(s // 2, m - 1)]
#
#     return any(h) if m % 2 != 0 else all(h)
#
#
# print('19', [s for s in range(18, 100) if f(s, 2)])  # 36
# print('20', [s for s in range(18, 100) if not f(s, 1) and f(s, 3)])  # 39 77
# print('21', [s for s in range(18, 100) if not f(s, 2) and f(s, 4)])  # 80


# txt = open('./txt/24-08-94.txt').read()
#
# txt = txt.replace('X', ' X')
# a = []
#
# for i in txt.split():
#     if i.count('Y') == 75:  # с помощью множества узнаем наибльшее кол-во 'Y'
#         a.append(i)
#
# print(len(min(a)) + 1)  # прибавляем 1 тк у нас отсекается один 'X' из всей строки из-за split()



















from itertools import *
from turtle import *
from ipaddress import *
from functools import *
from sys import *
from math import *


# 2
def f(w, x, y, z):
    return ((y <= (not (x <= z))) or w)


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(a1, 0, a2, a3), (0, 1, a4, a5), (1, a6, a7, 0)]
    for p in permutations('wxyz'):
        if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
            print(p)


# 5
for n in range(13):
    r = f'{n:b}'
    if n % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    print(n, r, int(r, 2))


# 6
tracer(0)
screensize(10_000, 10_000)
k = 50
left(90)

pd()
for r in range(3):
    forward(7 * k)
    right(90)
    forward(12 * k)
    right(90)
pu()

forward(4 * k)
right(90)
forward(6 * k)
left(90)

pd()
for r in range(4):
    forward(83 * k)
    right(90)
    forward(77 * k)
    right(90)
pu()

for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x * k, y * k)
        dot(5)

done()


# 8
counter = 0
for p in product('КОСУФ', repeat=5):
    s = ''.join(p)
    counter += 1
    if ('Ф' not in s) and (s.count('У') == 2):
        print(counter, s)


# 9
file = open('../txt/9/9-2024.txt')
counter = 0

for f in file:
    lst = [int(i) for i in f.split()]
    a3 = [i for i in lst if lst.count(i) == 3]
    a1 = [i for i in lst if lst.count(i) == 1]
    if len(a3) == len(a1) == 3:
        if (sum(a3)) ** 2 > (sum(a1)) ** 2:
            counter += 1

print(counter)


# 12
s = 83 * '8'
while '111' in s or '88888' in s:
    if '111' in s:
        s = s.replace('111', '88', 1)
    else:
        s = s.replace('88888', '8', 1)
print(s)


# 13
counter = 0
net = ip_network('112.160.0.0/255.240.0.0')
for ip in net:
    a = f'{ip:b}'
    if a.count('1') % 3 != 0:
        counter += 1

print(counter)


# 14
def f(n):
    seven = ''
    while n > 0:
        seven += str(n % 7)
        n //= 7
    return seven[::-1]


for x in range(1, 2031):
    s = (7 ** 91) + (7 ** 160) - x
    if f(s).count('0') == 70:
        print(x, f(s))


# 16
setrecursionlimit(1000000)
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * f(n - 1)


for i in range(10_000):
    f(i)

print((f(2024) // 16 - f(2023)) // f(2022))


# 17
file = open('../txt/17/17-2024.txt').read().split()
a32 = [int(i) for i in file if int(i) % 32 == 0]
lst = []

for i in range(len(file) - 2):
    if int(file[i]) < 0 or int(file[i + 1]):
        duo_summ = int(file[i]) + int(file[i + 1])
        if duo_summ < len(a32):
            lst.append(duo_summ)

print(len(lst), max(lst))


# 19-21
def f(s, m):
    if s >= 58:
        return 1
    if m == 0:
        return 0

    h = [f(s + 1, m - 1), f(s + 4, m - 1), f(s * 2, m - 1)]

    return any(h) if m % 2 != 0 else all(h)


print('19', [s for s in range(1, 58) if f(s, 2)])
print('20', [s for s in range(1, 58) if not f(s, 1) and f(s, 3)])
print('21', [s for s in range(1, 58) if not f(s, 2) and f(s, 4)])


# 23
def f(s, e):
    if s > e: return 0
    if s == e: return 1
    if s < e:
        return f(s + 1, e) + f(s + 2, e) + f(s + 3, e)


print(f(5, 7) * f(7, 11))

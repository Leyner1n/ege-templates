# imports
# ================================================================
from itertools import *
from turtle import *
from math import *
# ================================================================

print('===' * 10)

# 2
# ================================================================
# def f(u, w, x, y):
#     return (x <= w) <= (u <= y)

# for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
#     table = [(a1, a2,  1, 0), (a3, 1, 0, a4), (a5, a6, 1, 0)]
#     if len(table) == len(set(table)):
#         for p in permutations('uwxy'):
#             if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
#                 print(p) # xuwy
# ================================================================


# 5
# ================================================================
# lst = []

# for n in range(33, 100):
#     b = f'{n:b}'
#     if n % 2 != 0:
#         b = '1' + b[:-2] + '10'
#     else:
#         b = '10' + b[2:] + '1'

#     lst.append(int(b, 2))

# print(min(lst)) # 65
# ================================================================


# 6
# ================================================================
# left(90)
# c = 100
# tracer(0)
# screensize(10000, 10000)

# pd()

# for _ in range(49):
#     right(60)
#     forward(7 * c)
#     right(60)

# pu()

# for x in range(-40, 40):
#     for y in range(-40, 40):
#         setpos(x * c, y * c)
#         dot(5)

# done() # 24
# ================================================================


# 8
# ================================================================
# k = 0

# for x in product('0123456789abc', repeat=7):
#     s = ''.join(x)

#     if s[0] != '0' and s.count('5') >= 2:
#         for c in '2468ac': s = s.replace(c, '0')
#         for c in '3579b': s = s.replace(c, '1')
        
#         if '00' not in s or '11' not in s:
#             k += 1

# print(k)
# ================================================================


# 9
# ================================================================
# counter = 0
#
# for file in open('./txt/9.txt'):
#     text = [int(num) for num in file.split()]
#     answer_1 = [num for num in text if num % 2 == 0]
#     answer_2 = [num for num in text if num % 2 != 0]
#
#     if len(answer_1) >= 2 and len(answer_2) >= 2 and 3 * sum(answer_2) > prod(answer_1):
#         counter += 1
#
# print(counter) # 160
# ================================================================


# 12
# ================================================================
# for x in range(1, 50):
#     for y in range(1, 50):
#         for z in range(1, 50):
#             s = '>' + x * '1' + y * '2' + z * '3'

#             while '>1' in s or '>2' in s or '>3' in s:
#                 s = s.replace('>1', '21>3', 1)
#                 s = s.replace('>2', '32>', 1)
#                 s = s.replace('>3', '11>2', 1) 

#                 if s.count('1') == 71:
#                     if s.count('2') == 54:
#                         if s.count('3') == 37:
#                             print(f'единиц: {x};', f'двоек: {y};', f'троек: {z};', '===' * 10,  sep='\n')
#                             exit()
# =============================================


# 14
# ================================================================
# for x in range(401, 2000):
#     a = 16 ** 560 + 16 ** 120 - x
#     h = hex(a)[2:]
#     if h.count('0') == 442:
#         print(x) # 512
# ================================================================


# 16
# ================================================================
# def f(n):
#     k = 1
#     if n >= 1:
#         k += 1
#         k += f(n - 1)
#         k += f(n // 2)
#     return k

# print(f(40)) # 12370
# ================================================================


# 17
# ================================================================
# a = [int(x) for x in open('./txt/17.txt')]
# m = min(x for x in a if x % 2025 == 0)

# lst = []
# for i in range(len(a) - 2):
#     if (a[i] % m == 0 or a[i + 1] % m == 0 or a[i + 2] % m == 0):
#         w = a[i] + a[i + 1] + a[i + 2]
#         if 100_000 <= w < 1_000_000:
#             lst.append(w)

# print(len(lst), max(lst)) # 963 282747
# ================================================================


# 19-21
# ================================================================
def f(a, b, m):
    if a + b <= 33:
        return m % 2 == 0
    if m == 0:
        return 0
    
    h = [f(a - 2, b, m - 1), f(a, b - 2, m - 1),]
    if a > b:
        h.append(f(a // 2 + 1, b, m - 1))
    else:
        h.append(f(a, b // 2 + 1, m - 1))

    return any(h) if m % 2 != 0 else all(h)

print('19:', [b for b in range(11, 200) if f(23, b, 2)]) # 42
print('20:', [b for b in range(11, 200) if not f(23, b, 1) and  f(23, b, 3)]) # 24 46
print('21:', [b for b in range(11, 200) if not f(23, b, 2) and f(23, b, 4)]) # 28

# мои ответы: 
# 19: с any() == 41
# 20: 24 45
# 21: 47
# ================================================================

print('===' * 10)

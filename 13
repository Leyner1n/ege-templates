from functools import *


def f(curr, end):
    if curr > end or curr == 14:
        return 0
    if curr == end:
        return 1
    if curr < end:
        return f(curr + 1, end) + f(curr + 3, end)

print(f(2, 9) * f(9, 18))  # 63

def f(c, e):
    if c > e: return 0
    if c == e: return 1
    if c < e:
        return f(c + 1, e) + f(c + 3, e) + f(c * 2, e)

print(f(3, 10) * f(10, 20) * f(20, 30))
# 11368


def f(c, e):
    if c > e: return 0
    if c == e: return 1
    if c < e:
        return f(c + 1, e) + f(c + 2, e)

print(f(3, 15) + f(3, 14))


def f(c, e):
    if c < e: return 0
    if c == e: return 1
    if c > e:
        return f(c - 1, e) + f(c - 3, e) + f(c // 3, e)

print(f(22, 2))  # 2196


def f(c, e):
    if c > e or c == 21: return 0
    if c == e: return 1
    if c < e:
        return f(c + 1, e) + f(2 * c + 1, e)

print(f(1, 25))  # 20


def f(c, e):
    if c < e: return 0
    if c == e: return 1
    if c > e:
        return f(c - 8, e) + f(c // 2, e)

print(f(102, 43) * f(43, 5))  # 8


@lru_cache(None)
def f(c, e):
    if c > e: return 0
    if c == e: return 1
    if c < e:
        return f(c + 1, e) + f(2 * c, e) + f(2 * c + 1, e)

print(f(4, 218))  # 707420


def f(c, e):
    if c > e: return 0
    if c == e: return 1
    if c < e:
        if c % 2 == 0:
            return f(c + 1, e) + f(c * 2, e)
        return  f(c * 2, e)

print(f(3, 21))  # 0


def f(c, e):
    if c > e: return 0
    if c == e: return 1
    if c < e:
        return f(c + 1, e) + f(c + 5, e) + f(c * 3, e)


# ЕСЛИ ПРОСЯТ НАЙТИ КОЛ-ВО ПРОГ
for i in range(2, 200):
    if f(1, i)  == 175:
        print(i)  # 19
        break


def f(start, stop, step):
    if start > stop: return 0
    if start == stop and step == 6: return 1
    if start == stop and step != 6: return 0
    if start < stop:
        return (
                f(start + 1, stop, step + 1)
                + f(start + 2, stop, step + 1)
                + f(start * 2, stop, step + 1)
                )

print(f(1, 20, 0))  # 36

from functools import lru_cache


'''
def f(s, m):
    if s >= 34:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s + 1, m - 1), f(s + 2, m - 1), f(s + 3, m - 1), f(s * 2, m - 1)]
    return any(h) if m % 2 != 0 else all(h)


print('19', [s for s in range(1, 34) if f(s, 2)])
print('20', [s for s in range(1, 34) if not(f(s, 1)) and f(s, 3)])
print('21',  [s for s in range(1, 34) if not(f(s, 2)) and f(s, 4)])
'''

'''
def f(s, m, p): # "p" предыдущий ход

    if s >= 140:
        return m % 2 == 0
    if m == 0:
        return 0

    h = [] # значение функции для следующих ходов

    if p != '+1':
        h += [f(s + 1, m - 1, '+1')]
    if p != '+2':
        h += [f(s + 2, m - 1, '+2')]
    if p != '*3':
        h += [f(s * 3, m - 1, '*3')]

    return any(h) if m % 2 != 0 else all(h)


print('19', [s for s in range(1, 140) if f(s, 2, '')]) # 46
# в 20 спрашивается min и max значение s
print('20', [s for s in range(1, 140) if not (f(s, 1, '')) and f(s, 3, '')]) # 16, 45
print('21', [s for s in range(1, 140) if not f(s, 2, '') and f(s, 4, '')]) # 15
'''


'''
def f(s, m, p1, p2):
    if s >= 121: return m % 2 == 0
    if m == 0: return 0

    h = []

    if p2 != '+2': h += [f(s + 2, m - 1, '+2', p1)]
    if p2 != '+5': h += [f(s + 5, m - 1, '+5', p1)]
    if p2 != '+12': h += [f(s + 12, m - 1, '+12', p1)]
    if p2 != '*2': h += [f(s * 2, m - 1, '*2', p1)]

    return any(h) if m % 2 != 0 else all(h)


print('19:', min([s for s in range(1, 121) if f(s, 2, '', '')])) # 31 при any()
print('20:', min([s for s in range(1, 121) if (not (f(s, 1, '', ''))) and f(s, 3, '', '')])) # 47
print('21:', [s for s in range(1, 121) if (not(f(s, 4, '', ''))) and f(s, 6, '', '')]) # 35 46
'''


'''
def f(s, m):
    if s >= 22: return m % 2 == 0
    if m == 0: return 0

    h = [f(s + 1, m - 1), f(s + 2, m - 1)]

    if s % 2 != 0:
        h += [f(s * 2, m - 1)]

    return any(h) if m % 2 != 0 else all(h)


print('19:', [s for s in range(1, 22) if (not (f(s, 2))) and f(s, 4)]) # 14
print('20:', [s for s in range(1, 22) if (not (f(s, 1))) and f(s, 3)]) # 9 16
print('21:', [s for s in range(1, 22) if (not (f(s, 3))) and f(s, 5)]) # 7
'''
'''
def f(s, m):
    if 36 <= s <= 60: return m % 2 == 0
    if s > 60: return m % 2 != 0
    if m == 0: return 0

    h = [f(s + 1, m - 1), f(s * 2, m - 1), f(s * 3, m - 1)]

    return any(h) if m % 2 != 0 else all(h)


print('19:', [s for s in range(1, 36) if f(s, 2)])
print('20:', [s for s in range(1, 36) if not f(s, 1) and f(s, 3)])
print('21:', [s for s in range(1, 36) if not f(s, 2) and f(s, 4)])

'''
'''
def f(s1, s2, m):
    if s1 + s2 >= 59: return m % 2 == 0
    if m == 0: return 0

    h = [f(s1 + 1, s2,  m - 1), f(s1 * 2, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1, s2 * 2, m - 1)]

    return any(h) if m % 2 != 0 else all(h)


print('19:', [s for s in range(1, 53) if f(5, s, 1)])
print('20:', [s for s in range(1, 53) if not f(5, s, 1) and f(5, s, 3)])
print('21:', [s for s in range(1, 53) if not f(5, s, 2) and f(5, s, 4)])

'''


'''def f(s1, s2, m):
    if s1 + s2 > 76: return m % 2 == 0
    if m == 0: return 0

    h = [f(s1 + 1, s2, m - 1), f(s1 * 2, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1, s2 * 2, m - 1)]

    return any(h) if m % 2 != 0 else all(h)


print('19:', [s for s in range(1, 70) if f(7, s, 2)])
print('20:', [s for s in range(1, 70) if not f(7, s, 1) and f(7, s, 3)])
print('21:', [s for s in range(1, 70) if not f(7, s, 2) and f(7, s, 4)])
'''

'''
def f(a, b, m):
    if a + b >= 68:
        return m % 2 == 0
    if m == 0:
        return 0

    h = [f(a + 1, b, m - 1), f(a + b, b, m - 1), f(a, b + 1, m - 1), f(a, b + a, m - 1)]

    return any(h) if m % 2 != 0 else all(h)


print('19:', [s for s in range(1, 60) if f(8, s, 2)]) # 18
print('20:', [s for s in range(1, 60) if not f(8, s, 1) and f(8, s, 3)])
print('21:', [s for s in range(1, 60) if not f(8, s, 2) and f(8, s, 4)])

'''

'''
def f(a, b, m):
    if a * b >= 63:
        return m % 2 == 0
    if m == 0:
        return 0

    h = [f(a + 1, b, m - 1), f(a * 2, b, m - 1), f(a, b + 1, m - 1), f(a, b * 2, m - 1)]

    return any(h) if m % 2 != 0 else all(h)


print('19:', [s for s in range(1, 32) if f(2, s, 2)])
print('20:', [s for s in range(1, 32) if not f(2, s, 1) and f(2, s, 3)])
print('21:', [s for s in range(1, 32) if not f(2, s, 2) and f(2, s, 4)])

'''
'''


# 3 КУЧИ

def f(a, b, c, m):
    if a + b + c >= 73:
        return m % 2 == 0
    if m == 0:
        return 0

    h = [
            f(a + 3, b, c, m - 1), f(a, b + 3, c, m - 1), f(a, b, c + 3, m - 1),
            f(a + 13, b, c, m - 1), f(a, b + 13, c, m - 1), f(a, b, c + 13, m - 1),
            f(a + 23, b, c, m - 1), f(a, b + 23, c, m - 1), f(a, b, c + 23, m - 1)
        ]

    return any(h) if m % 2 != 0 else all(h)


print('19:', [s for s in range(1, 24) if f(2, s, s * 2, 2)]) # 9
print('20:', [s for s in range(1, 24) if not f(2, s, s * 2, 1) and f(2, s, s * 2, 3)])
print('21:', [s for s in range(1, 24) if not f(2, s, s * 2, 2) and f(2, s, s * 2, 4)])
'''

'''
@lru_cache(None)
def f(a, b, m):
    if a + b <= 20:
        return m % 2 == 0
    if m == 0:
        return 0

    h = [f(a - 1, b, m - 1), f(a, b - 1, m - 1), f((a + 1) // 2, b, m - 1), f(a, (b + 1) // 2, m - 1)]

    return any(h) if m % 2 != 0 else all(h)


print('19:', [s for s in range(10, 200) if f(10, s, 2)])
print('20:', [s for s in range(10, 200) if not f(10, s, 1) and f(10, s, 3)])
print('21:', [s for s in range(10, 200) if not f(10, s, 2) and f(10, s, 4)])

'''


# @lru_cache(None)
def f(s, m):
    if s >= 2163:
        return m % 2 == 0
    if m == 0:
        return 0

    h = [f(s + 1, m - 1), f(s * 3, m - 1)]

    return any(h) if m % 2 != 0 else all(h)


print('19:', [s for s in range(1, 2164) if f(s, 2)])
print('20:', [s for s in range(1, 2164) if not f(s, 1) and f(s, 3)])
print('21:', [s for s in range(1, 2164) if not f(s, 2) and f(s, 4)])

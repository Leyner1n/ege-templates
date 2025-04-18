def f(c, e):
    if c > e: return 0
    if c == e: return 1
    if c < e:
        return f(c + 1, e) + f(c * 1.5, e) if c % 2 == 0 else f(c + 1, e)


print(f(1, 20))


def f(c, e):
    if c > e:
        return 0
    if c == e:
        return 1
    if c < e:
        return f(c + 1, e) + f(c * 2, e)


print(f(1, 12) * f(12, 30))


def f(c, e):
    if c > e:
        return 0
    if c == e:
        return 1
    if c < e:
        return f(c + 1, e) + f(c + 3, e) + f(c * 2, e)


print(f(3, 9) * f(9, 12) * f(12, 20))


def f(c, e):
    if c < e:
        return 0
    if c == e:
        return 1
    if c > e:
        return f(c - 8, e) + f(c // 2, e)


print(f(102, 43) * f(43, 5))


def f(c, e):
    if c > e or c == 6: return 0
    if c == e: return 1
    if c < e:
        return f(c + 2, e) + f(c * 3, e)


print(f(1, 25) * f(25, 63))


def f(c, e):
    if c > e or c == 11 or c == 18: return 0
    if c == e: return 1
    if c < e:
        return f(c + 1, e) + f(c + 2, e) + f(c * 3, e)


print(f(4, 8) * f(8, 23))


def f(c, e):
    if c > e: return 0
    if c == e: return 1
    if c < e:
        return f(c + 1, e) + f(c * 2, e) + f(c * 2 + 1, e) + f(c * 10, e)


print(f(1, 15))


def f(c, e):
    if c > e or c == 43: return 0
    if c == e: return 1
    if c < e:
        return f(c + 2, e) + f(c + c - 1, e) + f(c + c + 1, e)


print(f(7, 63))


def f(c, e):
    int_c = int(c, 2)
    int_e = int(e, 2)
    if int_c > int_e:
        return 0
    if c == e:
        return 1
    if int_c < int_e:
        pass
        a1 = bin((int(c, 2) + 1))[2:]
        return f(a1, e) + f(c + '0', e) + f(c + '1', e)


print(f('100', '11101'))


def f(c, e):
    if c > e: return 0
    if c == e: return 1
    if c < e:
        if c % 10 == 9:
            a1 = 10
        else:
            a1 = 11
        return f(c + 1, e) + f(c + a1, e)


print(f(25, 51))


def f(c, e):
    if c > e:
        return 0
    if c == e:
        return 1
    if c < e:
        return f(c + 2, e) + f(c + 4, e) + f(c + 5, e)


for i in range(31, 100):
    if f(31, i) == 1001:
        print(i)


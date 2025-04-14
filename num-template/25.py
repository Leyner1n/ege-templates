# ДЕЛИТЕЛИ

# def div(x):
#     d = set()
#     for i in range(1, int(x ** 0.5) + 1):
#         if x % i == 0:
#             d.add(i)
#             d.add(x//i)
#     return sorted(d)
#
#
# for x in range(244143, 367821 + 1):
#     d = div(x)
#     if len(d) == 5:
#         print(d)


# def f(x):
#     d = set()
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             d |= {i, x // i}
#     return sorted(d)
#
#
# for x in range(135790, 163228 + 1):
#     d = f(x)
#     if sum(d) > 460_000:
#         print(len(d), sum(d))


# def f(x):
#     a = set()
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             a |= {i, x // i}
#     return sorted(a)
#
#
# for x in range(850000, 900000):
#     a = f(x)
#     if len(a): m
#         F = max(a) - min(a)
#         if F != 0 and F % 3 == 0:
#             print(x, F)


# def f(x):
# #     a = set()
# #     for i in range(2, int(x ** 0.5) + 1):
# #         if x % i == 0:
# #             a |= {i, x / i}
#     return sorted(a)
#
#
# for x in range(1_500_001, 1_500_300):
#     a = f(x)
#     if len(a):
#         F = sum(a) // len(a)
#         if F % 10 == 9:
#             print(x, F)


# def f(x):
#     a = set()
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             a |= {i, x // i}
#     return sorted(a)
#
#
# for x in range(300_000_000, 300_100_000):
#     a = f(x)
#     if len(a) >= 5:
#         P = a[0] * a[1] * a[2] * a[3] * a[4]
#         if P % 100 == 31 and P <= x:
#             print(P, a[4])


# def f(x):
#     a = set()
#     for i in range(1, int(x ** 0.5) + 1):
#         if x % i == 0:
#             a |= {i, x // i}
#     return sorted(a)
#
#
# for x in range(250_000, 250_201):
#     a = [i for i in f(x) if i % 2 == 0]
#     if len(a) == 6:
#         print(a[4], a[5])


# def f(x):
#     a = set()
#     for i in range(1, int(x ** 0.5) + 1):
#         if x % i == 0:
#             a |= {i, x // i}
#     return sorted(a)
#
#
# for x in range(333555, 777999 + 1):
#     a = [i for i in f(x) if len(str(i)) == 2]
#     if len(a):
#         if len(a) == 35:
#             print(x, min(a), max(a))
































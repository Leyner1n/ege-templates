from itertools import *

# counter = 1
# lst = []
# for p in product('ГОНДУБШ', repeat=6):
#     w = ''.join(p)
#     if w[0] != 'Б' and w.count('Н') >= 2 and 'У' not in w:
#         lst.append((counter, w))
#     counter += 1
#
#
# print(*lst, sep='\n')

# lst = []
# counter = 1
# for p in product('ДЛМОУЬ', repeat=6):
#     w = ''.join(p)
#     if p[0] == 'М' and counter % 2 != 0:
#         lst.append((counter, w))
#     counter += 1
#
# print(*lst, sep='\n')
# print(len(lst))


# lst = []
# count = 0
# for p in product('ЖКМФЦЧ', repeat=6):
#     w = ''.join(p)
#     if w.count('Ч') >= 2:
#         count += 1
#
# print(count)


# count = 1
# for p in product('АБРТЫ', repeat=5):
#     w = ''.join(p)
#     if w.count('Ы') == 0 and 'АА' not in w:
#         print(count)
#     count += 1

#
# count = 0
# for p in product('БЕЛКА', repeat=4):
#     w = ''.join(p)
#     if w.count('Б') == 1:
#         count += 1
#
# print(count)

# lst = []
# c = 0
# for p in product('АБВДОС', repeat=5):
#     w = ''.join(p)
#     lst.append(w)
#     if w == 'ОСОБА':
#         print(c, w)
#     if w == 'СДОБА':
#         print(c, w)
#     c += 1
#
# print(lst[6414], sep='\n')
# print(lst[7278], sep='\n')
#
# t = 0
# for i in lst[6414:7278]:
#     if len(i) == len(set(i)):
#         t += 1
#
# print(t)

#
# counter = 0
# for p in product('ДРАКОН', repeat=8):
#     w = ''.join(p)
#     if w.count('А') == 1 and w.count('О') == 1:
#         counter += 1
#
# print(counter)


# counter = 1
# gl = 'ЕИЮ'
# sogl = 'БДЖКНТ'
# lst =[]
# for p in product('БДЕЖИКНТЮ', repeat=6):
#     w = ''.join(p)
#     if w == 'БЮДЖЕТ':
#         break
#     W = ''
#     for a in w:
#         if a in gl:
#             W += '1'
#         else:
#             W += '0'
#     if not ('11' in W or '00' in W):
#         lst.append(counter)
#     counter += 1
# print(sum(lst))


# c = 1
# lst = []
# for p in product('БМНРЮ', repeat=6):
#     w = ''.join(p)
#     if w[0] != 'М' and w.count('Р') >= 2 and 'Ю' not in w:
#         lst.append(c)
#     c += 1
#
# print(*lst, sep='\n')


c = 0
for p in product('', repeat=5):
    w = int(p, 14)
    print(w)
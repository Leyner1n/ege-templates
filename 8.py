from itertools import *


s = 'АИЕ'
counter = 0
for p in product('КАБИНЕТ', repeat=7):
    w = ''.join(p)
    if len(w) == len(set(w)) and w[-1] not in s:

        counter += 1

print(counter)

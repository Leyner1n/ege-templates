from math import *


data = []
for s in open('.//27_A_21932.txt'):
    x, y = [float(d) for d in s.split()]
    data.append([x, y])

clusters = []
while data:
    cl = [data.pop()]
    for p in cl:
        sosed = [p1 for p1 in data if dist(p, p1)<1]
        for p1 in sosed:
            cl.append(p1)
            data.remove(p1)
    clusters.append(cl)

print([len(cl)] for cl in clusters)


def center(cl):
    m = []
    for p in cl:
        s = sum(dist(p, p1) for p1 in cl)
        m.append([s, p])
    return min(m)[1]


cen = [center(cl) for cl in clusters]
print(cen)

px = sum(x for x, y in cen) / len(cen)
py = sum(y for x, y in cen) / len(cen)
print('#координаты сред-арифм')
print(int(px * 10_000), int(py * 10_000))


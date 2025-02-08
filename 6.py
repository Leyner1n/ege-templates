from turtle import *


'''
tracer(0)  # отключение анимации
left(90)  # постановка координат
k = 20  # постановка размера
screensize(700, 700)  # масштаб

# код
for _ in range(6):
    forward(7 * k)
    right(120)

pd()  # поднять хвост

forward(3 * k)
right(90)

pu()  # опустить хвост

# код
for _ in range(8):
    forward(5 * k)
    right(90)


for x in range(-60, 60):
    for y in range(-60, 60):
        goto(x * k, y * k)
        dot(5)

done()
'''

# Если надо посчитать количество точек внутри фигуры

# speed(1000)
# m = 100
#
# screensize(3000, 3000)
#
# begin_fill()
# left(90)
# right(45)
#
# for i in range(2):
#     forward(5 * m)
#     right(45)
#     forward(10 * m)
#     right(135)
# end_fill()
#
# convas = getcanvas()
# cnt = 0
# for x in range(-200, 200):
#     for y in range(-200, 200):
#         if convas.find_overlapping(x * m, y * m, x * m, y * m) == (5,):
#             cnt += 1
#
# print(cnt)
# done()

# speed(1000)
# m = 100
# screensize(10_000, 10_000)
#
# begin_fill()
# left(90)
#
# for i in range(15):
#     forward(40 * m)
#     right(90)
#     forward(35 * m)
#     right(90)
# end_fill()
#
# convas = getcanvas()
# c = 0
# for x in range(-200, 200):
#     for y in range(-200, 200):
#         if convas.find_overlapping(x * m, y * m, x * m, y * m) == (5,):
#             c += 1
#
# print(c)
# done()


# Если надо посчитать количество точек внутри И НА ГРАНИЦАХ фигуры


# speed(1000)
# m = 100
#
# screensize(3000, 3000)
#
# begin_fill()
# left(90)
# right(45)
#
# for i in range(2):
#     forward(5 * m)
#     right(45)
#     forward(10 * m)
#     right(135)
# end_fill()
#
# convas = getcanvas()
# cnt = 0
# for x in range(-200, 200):
#     for y in range(-200, 200):
#         if convas.find_overlapping(x * m, y * m, x * m, y * m) != ():
#             cnt += 1
#
# print(cnt)
# done()


# Подсчет точек вручнеую

# tracer(0)
# k = 50
# pd()
# for i in range(24):
#     forward(3 * k)
#     left(60)
#
# pu()
#
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         setpos(x * k, y * k)
#         dot(5)
#
# done()


# автомат

# tracer(0)
# k = 40
# pd()
#
# begin_fill()
# for i in range(6):
#     forward(3 * k)
#     left(60)
# end_fill()
#
# pu()
#
# counter = 0
# canvas = getcanvas()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
#             counter += 1
# print(counter)
# done()


# tracer(0)
# k = 100
# left(90)
#
# pd()
#
# begin_fill()
# for i in range(111):
#     forward(123 * k)
#     right(120)
# end_fill()
#
# c = 0
# canvas = getcanvas()
# for x in range(-300, 300):
#     for y in range(-300, 300):
#         if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5, ):
#             c += 1
#
# print(c)
# done()


# tracer(0)
# k = 100
# left(90)
# screensize(10_000, 10_000)
#
# pd()
#
# begin_fill()
# for i in range(2):
#     right(90)
#     forward(120 * k)
#     right(90)
#     forward(14 * k)
# end_fill()
#
# pu()
#
# c = 0
# canvas = getcanvas()
#
# for x in range(-200, 200):
#     for y in range(-200, 200):
#         if canvas.find_overlapping(x * k, y * k, x * k, y * k) != ():
#             c += 1
#
# print(c)
# done()


tracer(0)
k = 200
left(90)
screensize(3000, 3000)

pd()

begin_fill()
for i in range(2):
    right(60)
    forward(7 * k)
    right(60)
end_fill()

pu()

counter = 0
canvas = getcanvas()

for x in range(-150, 150):
    for y in range(-150, 150):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5, ):
            counter += 1

print(counter)
done()







































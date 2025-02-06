from turtle import *


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

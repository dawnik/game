import turtle
import math

tim = turtle.Turtle()

length_side = 80

def square():
    for i in range(4):
        tim.forward(length_side)
        tim.left(90)

def board_game():
    for i in range(3):
        for j in range(3):
            tim.pd()
            square()
            tim.pu()
            tim.fd(length_side)
        tim.bk(3*length_side)
        tim.left(90)
        tim.forward(length_side)
        tim.right(90)
def cross(a, b):
    tim.pu()
    tim.setx(a*length_side + length_side/2)
    tim.sety(b*length_side + length_side/2)
    tim.pd()
    tim.left(45)
    for i in range(4):
        tim.fd(length_side/4)
        tim.bk(length_side/4)
        tim.left(90)
    tim.right(45)
    tim.pu()

def ring(a, b):
    tim.pu()
    tim.setx(a * length_side + length_side / 2)
    tim.sety(b * length_side + length_side / 2 - 54/math.pi)
    tim.pd()
    tim.left(45)
    for i in range(36):
        tim.fd(3)
        tim.left(10)
    tim.pu()

def reset():
    tim.home()


board_game()
turn = 0

print("Start")
while True:
    reset()
    a = int(input("Position x: "))
    b = int(input("Position y: "))
    if (turn % 2) == 0:
        ring(a,b)
    if (turn % 2) != 0:
        cross(a,b)
    turn += 1

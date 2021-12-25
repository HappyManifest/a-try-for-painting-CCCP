#生产地点: 杨浦公社技术部门
#生产时间: 2021/12/24 22:37
#生产者: 公社人民
#公社万岁
import turtle
from turtle import *

def main():
    speed('fastest')
    turtle.color('yellow')
    turtle.bgcolor('red')
    turtle.penup()
    turtle.goto(-150,-10)
    turtle.pendown()

    turtle.hideturtle()
    begin_fill()
    turtle.fillcolor('yellow')
    turtle.right(45)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(160)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(45)
    turtle.forward(141.4)
    turtle.right(135)
    turtle.forward(140)
    end_fill()

    turtle.hideturtle()
    penup()
    turtle.goto(-250,-300)
    pendown()
    begin_fill()
    turtle.fillcolor('yellow')
    right(180)
    forward(175)
    right(90)
    forward(2)
    for i in range(40):
        left(1)
        forward(2)
        i+=1
    for i in range(50):
        left(0.8)
        forward(3)
        i+=1
    for i in range(50):
        left(1.2)
        forward(2)
        i+=1
    for i in range(80):
        left(0.5)
        forward(2.5)
        i+=1
    for i in range(20):
        left(2)
        forward(1)
        i+=1
    left(130)
    for i in range(60):
        right(0.6)
        forward(2)
        i+=1
    for i in range(30):
        right(0.8)
        forward(3)
        i+=1
    for i in range(40):
        right(1.5)
        forward(2)
        i+=1
    for i in range(40):
        right(1)
        forward(2)
        i+=1
    forward(40)
    left(80)
    forward(175)
    left(90)
    forward(60)
    end_fill()

    turtle.hideturtle()
    penup()
    turtle.goto(0,200)
    pendown()
    begin_fill()
    turtle.forward(50)
    for i in range(1, 5) :
        turtle.left(72)
        turtle.forward(50)
        turtle.right(144)
        turtle.forward(50)
    goto(0,200)
    end_fill()

    penup()
    turtle.goto(100, 150)
    pendown()
    turtle.write('CCCP',font=("Comic Sans MS", 60, "bold"))
    penup()
    turtle.goto(-300,150)
    pendown()
    turtle.write('create by ZYQ',font=('Comic Sans MS',30))
    turtle.mainloop()
main()


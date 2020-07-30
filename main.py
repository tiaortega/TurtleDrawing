import turtle

#Shape Drawings
#--------------

t = turtle.Turtle()
t.color ("red")
t.fillcolor ("red")
t.begin_fill()
for i in range ( 0,8):
    t.forward(75)
    t.left(45)
t.end_fill()      

import math
a = 100
b = 100
c = math.sqrt( a*a+b*b )


t.penup()
t.right(45)
t.forward(100)
t.pendown()
t.color ("yellow")
t.fillcolor ("yellow")
t.begin_fill()
t.forward (a)
t.right(135)
t.forward (c)
t.right(135)
t.forward (b)
t.end_fill()


t.penup()
t.right(180)
t.forward(300)
t.pendown()
t.right (45)
t.color ("black")
t.fillcolor ("black")
t.begin_fill()
for p in range (0,4):
    t.forward(200)
    t.right (90)
t.end_fill()  
t.left(180)


t.penup()
t.forward(500)
t.pendown()
t.right (90)
t.color ("blue")
t.fillcolor ("blue")
t.begin_fill()
t.forward(50)
t.right (90)
t.forward (100)
t.right (90)
t.forward(50)
t.right (90)
t.forward (100)
t.end_fill()
t.left (90)


t.penup()
t.forward(600)
t.pendown()
t.left(90)
t.color ("green")
t.fillcolor ("green")
t.begin_fill()
r = 50
t.circle(r)
t.end_fill()

t.penup()
t.forward(600)
t.pendown()
t.pencolor("orange")
t.fillcolor('orange')
t.begin_fill()
for i in range(5):
  t.forward(90)
  t.left(144)
t.end_fill()
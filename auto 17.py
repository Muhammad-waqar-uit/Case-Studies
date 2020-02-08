def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
import turtle
s=turtle.Screen()
a=turtle.Turtle()
a.shape('circle')
b=turtle.Turtle()
b.shape('circle')
c=turtle.Turtle()
c.shape('circle')
d=turtle.Turtle()
d.shape('circle')
jump(a,0,-58)
jump(b,0,-108)
jump(c,0,-150)
jump(d,0,-228)
i=True
while i==True:
    a.speed(100)
    b.speed(100)
    c.speed(100)
    d.speed(100)
    for j in range(7):
        a.circle(58,1)
    for j in range(3):
        b.circle(108,1)
    for j in range(2):
        c.circle(150,1)
    for j in range(1):
        d.circle(228,1)

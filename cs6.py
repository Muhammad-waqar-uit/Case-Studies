import turtle
s=turtle.Screen()
t=turtle.Turtle()
def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
t.circle(25)
jump(t,0,-25)
t.circle(50)
jump(t,0,-50)
t.circle(75)
jump(t,0,-75)
t.circle(100)

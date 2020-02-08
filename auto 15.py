import turtle
s=turtle.Screen()
t=turtle.Turtle()
def Grid(X,Y):
    x=0
    y=0
    for i in range(X):
        for j in range(Y):
            t.penup()
            t.goto(x,y)
            t.pendown()
            Box()
            x+=75
        y-=75
        x=0
        t.penup()
        t.goto(x,y)
        t.pendown()

            
def Box():
    for i in range(4):
        t.forward(75)
        t.right(90)
Grid(2,2)

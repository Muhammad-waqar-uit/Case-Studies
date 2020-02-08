import turtle
s=turtle.Screen()
t=turtle.Turtle()
def polygon(t):
    n=int(input("enten the number of sides of polygon:"))
    for i in range(1,n+1):
        t.forward(100)
        t.left(35)
    t.goto(0,0)
polygon(t)

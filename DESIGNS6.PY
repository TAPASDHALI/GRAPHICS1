import turtle

t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)
s.bgcolor("black")
t.pencolor("purple")
c = 0
d = 0
while True:
    for i in range(4):
        t.forward(90)
        t.left(90)
        
    t.left(5)
    c += 1
    if c >= 360/5:
        t.forward(50)
        c = 0
        d += 1
        if d >= 5: 
            break
            

t.hideturtle()
turtle.done()

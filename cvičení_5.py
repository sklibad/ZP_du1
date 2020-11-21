from turtle import forward, exitonclick, left, right, penup, pendown, speed, setpos, circle, write
import math

a = 50
x = 3
y = 3
speed(9)
for i in range(y):
    for j in range(x):
        for k in range(5):
            forward(a)
            right(90)
        left(90)
    left(180)
    forward(x*a)
    left(90)
    forward(a)
    left(90)

while True:
    coord = input("Zadej souřadnici ve formátu 'X:Y':")
    if coord == 'k':
        break
    X = int(coord[0])
    Y = int(coord[2])
    penup()
    setpos(X*a,-Y*a)
    pendown()
    right(45)
    forward(math.sqrt(2*a**2))
    penup()
    setpos(X*a+a,-Y*a)
    pendown()
    right(90)
    forward(math.sqrt(2*a**2))
    left(135)
    
    coord = input("Zadej souřadnici ve formátu 'X:Y':")
    if coord == 'k':
        break
    X = int(coord[0])
    Y = int(coord[2])
    penup()
    setpos(a/2+X*a,-a-Y*a)
    pendown()
    circle(a/2)
write('Game over!',align="center",font=("Arial", 120, "normal"))
exitonclick()


from turtle import forward, exitonclick, left, right, position, speed, setposition
"""
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
exitonclick()

for i in range(4):
    forward(200)
    left(90)
exitonclick()

a = position()
forward(200)
b = position()
while a != b:
    left(90)
    forward(200)
    b = position()
    print(b)
exitonclick()

a = 150
for i in range(6):
    forward(a)
    left(60)
exitonclick()

b = 150
n = 4
angle = (1-2/n)*180
for i in range(n):
    forward(b)
    left(angle)
exitonclick()

#příklad 3
a = 150
for i in range(4):
    forward(a)
    left(90)
for j in range(4):
    forward(a)
    right(90)
for k in range(4):
    right(90)
    forward(a)
for k in range(4):
    left(90)
    forward(a)
exitonclick()

#příklad 4
b = 100
for i in range(6):
    forward(b)
    left(60)
for i in range(6):
    forward(b)
    right(60)
right(120)
for i in range(5):
    forward(b)
    right(60)
right(120)
for i in range(5):
    forward(b)
    right(60)
left(120)
for i in range(7):
    forward(b)
    left(60)
for i in range(5):
    forward(b)
    right(60)
right(120)
for i in range(4):
    forward(b)
    right(60)         
exitonclick()

#příklad 5
a = 50
x = 6
y = 8
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
exitonclick()
"""
#příklad 6
b = 100
x = 2
y = 3
z = 0
speed(6)

for i in range(x):
    for i in range(8):
        forward(b)
        left(60)
    right(120) 
right(120)
for i in range(x):
    forward(b)
    right(60)
    forward(b)
    left(60)
z = z + 1
setposition(0,-173.21*z)
exitonclick()
"""
#příklad 7

while True:
    a = int(input("Uhádni číslo od 1 do 10: "))
    if a < 7:
        print("Moc malé")
    elif a > 7:
        print("Moc velké")
    else:
        print("Vyhrál jsi!")
        break     
"""
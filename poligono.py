import turtle

t = turtle.Pen()

t.forward(50)
for i in range(3,14):
    angle = 360/i

    for j in range(i - 1):
        if i % 2 == 1:
            t.left(angle)
        else:
            t.right(angle)
        t.forward(50)
    if i % 2 == 0:
        t.left(180 - 360/i)
    else:
        t.right(180 - 360/i)
input()
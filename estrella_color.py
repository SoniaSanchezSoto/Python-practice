'''import turtle

window = turtle.Screen()
flecha = turtle.Turtle()

for i in range(4):
   flecha.forward(100)
   flecha.left(90)'''

from turtle import*
color('blue', 'green')
begin_fill()
while True:
    forward(300)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
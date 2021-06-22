from turtle import *
hideturtle()

def draw_star(sidesize, points, alfacorner, color):
    betacorner = 360/points+alfacorner
    fillcolor(color)
    begin_fill()
    for x in range(points*2):
        forward(sidesize)
        if x % 2 == 0:
            left(180-alfacorner)
        else:
            right(180-betacorner)
    end_fill()


draw_star(70, 8, 90, 'grey')
draw_star(90, 5, 72, 'yellow')
draw_star(120, 5, 36, 'red')
draw_star(65, 6, 60, 'darkblue')
draw_star(80, 4, 45, 'darkviolet')
draw_star(80, 3, 30, 'greenyellow')
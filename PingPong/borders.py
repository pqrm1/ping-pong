from turtle import Turtle

def bor():
    finish=Turtle()
    finish.color("white")
    finish.speed("fastest")
    finish.penup()

    lines = [
        [(-450, 430), (450, 430)],  # top
        [(-450, 430), (-450, -480)],  # left
        [(450, 430), (450, -480)],  # right
        [(-450, -480), (450, -480)]  # bottom
    ]

    for start,end in lines:
        finish.goto(start)
        finish.pendown()
        finish.goto(end)
        finish.penup()

    finish.goto(0,430)
    finish.pendown()
    finish.goto(0,-480)
    finish.penup()

    finish.hideturtle()
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 40
        if new_y>380:
            new_y=380
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 40
        if new_y<-418:
            new_y=-418
        self.goto(self.xcor(), new_y)

    def reset(self):
        self.goto(self.xcor(),0)



from turtle import Turtle
import time
import random
from score import Score

class Ball(Turtle):
    def __init__(self,score):
        self.score=score
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.mov_x=4
        self.mov_y=4

    def move(self):
        new_x=self.xcor()+self.mov_x
        new_y=self.ycor()+self.mov_y
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.mov_y*=-1

    def bounce_x(self):
        self.mov_x*=-1

    #collison with the top and bottom walls
    def collision(self):
        if self.ycor()>425 or self.ycor()<-475:
            self.bounce_y()

    def check_score(self,l,r):
        if  self.xcor()<-450:
            self.score.increase_r_score()
            self.hideturtle()
            self.reset_game(l,r)
        elif  self.xcor()>450:
            self.score.increase_l_score()
            self.hideturtle()
            self.reset_game(l,r)


    #collision with paddle
    def paddle_collision(self,l_paddle,r_paddle):
        if self.distance(l_paddle)<50 and self.xcor()<-380:
            self.bounce_x()

        elif self.distance(r_paddle)<50 and self.xcor()>380:
            self.bounce_x()

    #reset after points
    def reset_position(self):
        self.showturtle()
        self.goto(0,0)
        time.sleep(2)
        dirxn=[(-4,-2),(4,-2),(-4,2),(4,2)]
        self.mov_x,self.mov_y=random.choice(dirxn)



    def reset_game(self, l_paddle, r_paddle):
        self.reset_position()  # Reset ball to center + new direction
        l_paddle.reset()  # Left paddle back to center
        r_paddle.reset()  # Right paddle back to center

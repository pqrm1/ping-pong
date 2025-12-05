from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from borders import  bor
from score import Score

screen=Screen()
score=Score()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)

l_paddle=Paddle((-420,0))
r_paddle=Paddle((420,0))
ball=Ball(score)
bor()
score.update_score()


screen.listen()
screen.onkey(key='Up',fun=r_paddle.go_up)
screen.onkey(key='Down',fun=r_paddle.go_down)


screen.onkey(key='w',fun=l_paddle.go_up)
screen.onkey(key='s',fun=l_paddle.go_down)

game_on=True
while game_on:
    ball.move()


    ball.collision()
    ball.check_score(l_paddle,r_paddle)
    ball.paddle_collision(l_paddle,r_paddle)

    screen.update()
    time.sleep(0.01)
    if score.l_score==6 or score.r_score==6:
        score.g_over()
        game_on=False



screen.exitonclick()


from turtle import Turtle

ALIGN="center"
FONT=('Arial', 24, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.color("white")
        self.penup()
        self.goto(0, 450)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Left Score= {self.l_score} \t\t\t Right Score={self.r_score}", align=ALIGN, font=FONT)

    def increase_r_score(self):
        self.r_score+=1
        self.clear()
        self.update_score()

    def increase_l_score(self):
        self.l_score+=1
        self.clear()
        self.update_score()

    def g_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!!!", align=ALIGN, font=FONT)

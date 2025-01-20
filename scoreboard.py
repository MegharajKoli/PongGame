from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=Turtle()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score=0
        self.r_score=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 280)
        self.write(self.l_score, align="center", font=("courier", 50, "normal"))
        self.goto(100, 280)
        self.write(self.r_score, align="center", font=("courier", 50, "normal"))

    def l_point(self):
        self.l_score+=1
        self.update_scoreboard()

    def r_point(self):
        self.r_score+=1
        self.update_scoreboard()

    def l_winner(self):
        self.goto(-30,200)
        self.write("Winner is Left Player", align="center", font=("courier", 25, "normal"))

    def r_winner(self):
        self.goto(-30, 200)
        self.write("Winner is Right Player", align="center", font=("courier", 25, "normal"))
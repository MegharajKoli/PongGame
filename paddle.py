from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.paddle=Turtle()
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.penup()
        self.goto(position,0)

    def move_up(self):
        self.penup()
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def move_down(self):
        self.penup()
        new_y = self.ycor() -20
        self.goto(self.xcor(), new_y)
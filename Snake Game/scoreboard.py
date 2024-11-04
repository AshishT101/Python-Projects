from turtle import  Turtle
from food import Food

ALIGNMENT = "center"
FONT = "Arial"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.hideturtle()
        self.setposition(0,280)
        self.color("white")
        self.write(f"Score: {self.score} ", False, ALIGNMENT,(FONT, 10, 'normal') )


    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", False, 'center', ('Arial', 10, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


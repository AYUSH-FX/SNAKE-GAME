from turtle import Turtle
ALIGNMENT = "center"
FONT =("Arial", 24, "normal")

class ScoreBoard(Turtle) :
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("OOPS! GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_scorecard(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

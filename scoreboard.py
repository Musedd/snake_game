from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
TOP_CENTER = (0, 270)
SCREEN_MIDDLE = (0,0)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(TOP_CENTER)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    def increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(SCREEN_MIDDLE)
        self.write(arg="GAME OVER.", align=ALIGNMENT, font=FONT)







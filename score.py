from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as last_high_score:
            self.high_score = int(last_high_score.read())
        self.hideturtle()
        self.penup()
        self.sety(y=250)
        self.color("white")
        self.refresh()

    def refresh(self):
        self.clear()
        text = f"SCORE: {self.score}      HIGH SCORE: {self.high_score}"
        self.write(arg=text, move=False, align="center", font=("Arial", 20, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as last_high_score:
                last_high_score.write(str(self.high_score))
        self.score = 0
        self.refresh()

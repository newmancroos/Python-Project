from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score=0
        self.read_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(F"Score : {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def write_to_file(self):
        with open("data.txt","w") as file:
            file.write(str(self.high_score))

    def read_score(self):
        with open("data.txt", "r") as file:
            score_h= int(file.read())
            self.high_score = score_h

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_to_file()
            self.score =0
            self.update_scoreboard()

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(F"GAME OVER", align=ALIGNMENT, font=FONT)
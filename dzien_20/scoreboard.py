from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Times New Roman', 24, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.upade_score()

    def upade_score(self):
        self.clear()
        self.write(f'SCORE: {self.score} High Score: {self.high_score}', move=False, align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
           self.high_score = self.score
           with open('data.txt', mode='w') as data:
               data.write(f'{self.high_score}')
        self.score = 0
        self.upade_score()

    def score_count(self):
        self.score += 1
        self.upade_score()
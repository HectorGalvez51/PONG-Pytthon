from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.right = []
        self.left = []
        self.penup()
        self.right_paddle()
        self.left_padle()
        self.speed('fastest')
        self.right_head = self.right
        self.left_head = self.left[0]

    def new_paddle(self, position):
        paddle = Turtle(shape='square')
        paddle.color('white')
        paddle.penup()
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        if position == 'right':
            paddle.goto(520, 0)
            self.right.append(paddle)
        else:
            paddle.goto(-530, 0)
            self.left.append(paddle)

    def right_paddle(self):
        self.new_paddle('right')

    def left_padle(self):
        self.new_paddle('left')

    def up_right(self):
        if self.right[0].ycor() < 320:
            y_cord = self.right[0].ycor() + 20
            self.right[0].goto(self.right[0].xcor(), y_cord)

    def up_left(self):
        if self.left[0].ycor() < 320:
            y_cord = self.left[0].ycor() + 20
            self.left[0].goto(self.left[0].xcor(), y_cord)

    def down_right(self):
        if self.right[0].ycor() > -300:
            y_cord = self.right[0].ycor() - 20
            self.right[0].goto(self.right[0].xcor(), y_cord)

    def down_left(self):
        if self.left[0].ycor() > -300:
            y_cord = self.left[0].ycor() - 20
            self.left[0].goto(self.left[0].xcor(), y_cord)


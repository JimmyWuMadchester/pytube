from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, init_xcor, init_ycor, dy, yrange):
        super().__init__(shape="square")
        self.speed(0)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(init_xcor, init_ycor)
        self.yheight = 100
        self.yrange = yrange
        self.dy = dy

    def up(self):
        y = self.ycor()
        ceiling_y = (self.yrange - self.yheight)/2 - 5
        if y < ceiling_y:
            self.sety(y + self.dy)

    def down(self):
        y = self.ycor()
        floor_y = -(self.yrange - self.yheight)/2 + 10
        if y > floor_y:
            self.sety(y - self.dy)


class Ball(Turtle):
    def __init__(self, xrange, yrange):
        super().__init__(shape="circle")
        self.speed(0)
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 0.3
        self.dy = 0.3
        self.ceiling = yrange/2 - 10
        self.floor = -(yrange/2 - 10)
        self.left_wall = -(xrange/2 - 10)
        self.right_wall = xrange/2 - 10

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

        if self.hit_ceiling() or self.hit_floor():
            self.dy *= -1

    def reset_position_after_score(self):
        self.goto(0, 0)
        self.dx *= -1

    def bounce(self):
        self.dx *= -1
        self.move()

    def hit_ceiling(self):
        return self.ycor() >= self.ceiling

    def hit_floor(self):
        return self.ycor() <= self.floor

    def hit_left_wall(self):
        print(f"Ball xcor: {self.xcor()}")
        return self.xcor() <= self.left_wall

    def hit_right_wall(self):
        return self.xcor() >= self.right_wall

    def hit_paddle(self, paddle):
        hit_paddle_x = abs(self.xcor() - paddle.xcor()) < 10
        hit_paddle_y = abs(self.ycor() - paddle.ycor()) < paddle.yheight/2
        return hit_paddle_x and hit_paddle_y


class ScoreBoard(Turtle):
    def __init__(self, ycor):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, ycor)
        self.score_a = 0
        self.score_b = 0
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.write(f"Player A: {self.score_a} vs Player B: {self.score_b}",
                   align="center", font=("Courier", 24, "normal"))

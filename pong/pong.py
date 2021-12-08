import turtle
import shapes

# Constants
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
PADDLE_MOVEMENT_DELTA = 20

# Window
wn = turtle.Screen()
wn.title("Pong by @Y.W.")
wn.bgcolor("black")
wn.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
wn.tracer(0)

# Paddles
paddle_a = shapes.Paddle(-350, 0, PADDLE_MOVEMENT_DELTA, WINDOW_HEIGHT)
paddle_b = shapes.Paddle(350, 0, PADDLE_MOVEMENT_DELTA, WINDOW_HEIGHT)

# Ball
ball = shapes.Ball(xrange=WINDOW_WIDTH, yrange=WINDOW_HEIGHT)

# Scoreboard
scoreboard = shapes.ScoreBoard(260)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a.up, "w")
wn.onkeypress(paddle_a.down, "s")
wn.onkeypress(paddle_b.up, "Up")
wn.onkeypress(paddle_b.down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.move()
    if ball.hit_paddle(paddle_a) or ball.hit_paddle(paddle_b):
        ball.bounce()

    if ball.hit_left_wall():
        scoreboard.score_b += 1
        scoreboard.update_scores()
        ball.reset_position_after_score()

    if ball.hit_right_wall():
        scoreboard.score_a += 1
        scoreboard.update_scores()
        ball.reset_position_after_score()
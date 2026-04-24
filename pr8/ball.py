import random

from config import BALL_SIZE, BALL_SPEED_Y, BALL_START_X, BALL_START_Y, SCREEN_HEIGHT, SCREEN_WIDTH


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.size = BALL_SIZE
        self.hit_bottom = False

        self.id = canvas.create_oval(
            10,
            10,
            10 + self.size,
            10 + self.size,
            fill=color,
            outline=color,
        )
        self.canvas.move(self.id, BALL_START_X, BALL_START_Y)

        self.speed_x = random.choice([-3, -2, -1, 1, 2, 3])
        self.speed_y = BALL_SPEED_Y

    def hit_paddle(self):
        ball_left, ball_top, ball_right, ball_bottom = self.canvas.coords(self.id)
        paddle_left, paddle_top, paddle_right, paddle_bottom = self.canvas.coords(self.paddle.id)

        horizontal_hit = ball_right >= paddle_left and ball_left <= paddle_right
        vertical_hit = ball_bottom >= paddle_top and ball_top <= paddle_bottom

        return horizontal_hit and vertical_hit and self.speed_y > 0

    def draw(self):
        if self.hit_bottom:
            return

        self.canvas.move(self.id, self.speed_x, self.speed_y)
        left, top, right, bottom = self.canvas.coords(self.id)

        if left <= 0:
            self.speed_x = abs(self.speed_x)
        elif right >= SCREEN_WIDTH:
            self.speed_x = -abs(self.speed_x)

        if top <= 0:
            self.speed_y = abs(self.speed_y)

        if self.hit_paddle():
            paddle_left, _, paddle_right, _ = self.canvas.coords(self.paddle.id)
            ball_center_x = (left + right) / 2
            paddle_center_x = (paddle_left + paddle_right) / 2

            self.speed_y = -abs(self.speed_y)

            if ball_center_x < paddle_center_x:
                self.speed_x = -max(2, abs(self.speed_x))
            else:
                self.speed_x = max(2, abs(self.speed_x))

            self.canvas.move(self.id, 0, -4)

        if bottom >= SCREEN_HEIGHT:
            self.hit_bottom = True

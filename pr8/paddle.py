from config import (
    PADDLE_HEIGHT,
    PADDLE_SPEED,
    PADDLE_START_X,
    PADDLE_START_Y,
    PADDLE_WIDTH,
    SCREEN_WIDTH,
)


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.speed_x = 0
        self.id = canvas.create_rectangle(
            0,
            0,
            PADDLE_WIDTH,
            PADDLE_HEIGHT,
            fill=color,
            outline=color,
        )
        self.canvas.move(self.id, PADDLE_START_X, PADDLE_START_Y)

        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyRelease-Left>", self.stop_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)
        self.canvas.bind_all("<KeyRelease-Right>", self.stop_right)

    def move_left(self, _event=None):
        self.speed_x = -PADDLE_SPEED

    def stop_left(self, _event=None):
        if self.speed_x < 0:
            self.speed_x = 0

    def move_right(self, _event=None):
        self.speed_x = PADDLE_SPEED

    def stop_right(self, _event=None):
        if self.speed_x > 0:
            self.speed_x = 0

    def draw(self):
        self.canvas.move(self.id, self.speed_x, 0)
        left, _, right, _ = self.canvas.coords(self.id)

        if left < 0:
            self.canvas.move(self.id, -left, 0)
            self.speed_x = 0
        elif right > SCREEN_WIDTH:
            self.canvas.move(self.id, SCREEN_WIDTH - right, 0)
            self.speed_x = 0

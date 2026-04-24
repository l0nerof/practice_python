import tkinter as tk

from ball import Ball
from config import (
    BACKGROUND_COLOR,
    BALL_COLOR,
    FRAME_DELAY,
    PADDLE_COLOR,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    WINDOW_TITLE,
)
from paddle import Paddle


class JumpGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        self.root.resizable(False, False)
        self.root.wm_attributes("-topmost", 1)

        self.canvas = tk.Canvas(
            self.root,
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            bg=BACKGROUND_COLOR,
            bd=0,
            highlightthickness=0,
        )
        self.canvas.pack()

        self.root.bind("<Escape>", self.close_game)

        self.paddle = Paddle(self.canvas, PADDLE_COLOR)
        self.ball = Ball(self.canvas, self.paddle, BALL_COLOR)
        self.running = True
        self.game_over_text_id = None

    def close_game(self, _event=None):
        self.running = False
        self.root.destroy()

    def show_game_over(self):
        if self.game_over_text_id is None:
            self.game_over_text_id = self.canvas.create_text(
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2,
                text="Гра завершена!",
                font=("Helvetica", 28, "bold"),
                fill="red",
            )
            self.canvas.create_text(
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2 + 35,
                text="М'яч торкнувся нижньої межі. Натисніть Esc для виходу.",
                font=("Helvetica", 14),
                fill="black",
            )

    def update(self):
        if not self.running:
            return

        self.ball.draw()
        self.paddle.draw()

        if self.ball.hit_bottom:
            self.show_game_over()
            self.running = False
            return

        self.root.after(FRAME_DELAY, self.update)

    def run(self):
        self.update()
        self.root.mainloop()


if __name__ == "__main__":
    game = JumpGame()
    game.run()

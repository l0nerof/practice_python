import tkinter as tk

from config import (
    BACKGROUND_COLOR,
    FRAME_DELAY,
    PLAYER_COLOR,
    PLAYER_HEIGHT,
    PLAYER_START_X,
    PLAYER_START_Y,
    PLAYER_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TARGET_COLOR,
    TARGET_RADIUS,
    WINDOW_TITLE,
)
from player import Player
from target import Target


class Game:
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

        self.running = True
        self.message_id = None

        self.create_game_objects()
        self.bind_keys()

    def create_game_objects(self):
        self.player = Player(
            self.canvas,
            PLAYER_START_X,
            PLAYER_START_Y,
            PLAYER_WIDTH,
            PLAYER_HEIGHT,
            PLAYER_COLOR,
        )

        self.target = Target(self.canvas, TARGET_RADIUS, TARGET_COLOR)

        while self.player.collides_with(self.target.id):
            self.canvas.delete(self.target.id)
            self.target = Target(self.canvas, TARGET_RADIUS, TARGET_COLOR)

        self.canvas.create_text(
            SCREEN_WIDTH // 2,
            20,
            text="Керування: стрілки клавіатури",
            font=("Helvetica", 14),
            fill="black",
        )

    def bind_keys(self):
        self.root.bind("<KeyPress-Left>", self.player.move_left)
        self.root.bind("<KeyRelease-Left>", self.player.stop_horizontal)
        self.root.bind("<KeyPress-Right>", self.player.move_right)
        self.root.bind("<KeyRelease-Right>", self.player.stop_horizontal)
        self.root.bind("<KeyPress-Up>", self.player.move_up)
        self.root.bind("<KeyRelease-Up>", self.player.stop_vertical)
        self.root.bind("<KeyPress-Down>", self.player.move_down)
        self.root.bind("<KeyRelease-Down>", self.player.stop_vertical)

    def check_collisions(self):
        if self.player.collides_with(self.target.id):
            self.running = False
            self.show_win_message()

    def show_win_message(self):
        self.message_id = self.canvas.create_text(
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2,
            text="Ви виграли!",
            font=("Helvetica", 28, "bold"),
            fill="green",
        )

    def update(self):
        if not self.running:
            return

        self.player.move()
        self.check_collisions()

        if self.running:
            self.root.after(FRAME_DELAY, self.update)

    def run(self):
        self.update()
        self.root.mainloop()

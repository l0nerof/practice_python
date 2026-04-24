import random
import tkinter as tk

from catcher import Catcher
from egg import Egg
from score import Score


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
MAX_LOST = 5
SPAWN_CHANCE = 8
FRAME_DELAY = 30


class EggCatcherGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Гра: Ловець")
        self.root.resizable(False, False)
        self.root.wm_attributes("-topmost", 1)

        self.canvas = tk.Canvas(
            self.root,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            bd=0,
            highlightthickness=0,
            bg="white",
        )
        self.canvas.pack()

        self.score = Score(self.canvas)
        self.catcher = Catcher(self.canvas, "blue", self.score)
        self.eggs = []
        self.game_over = False

    def spawn_egg(self):
        if random.randint(1, 100) <= SPAWN_CHANCE:
            self.eggs.append(Egg(self.canvas, "red", self.score))

    def update(self):
        if self.game_over:
            return

        self.spawn_egg()
        self.catcher.draw()
        self.catcher.catch(self.eggs)

        for egg in list(self.eggs):
            if egg.draw():
                self.eggs.remove(egg)

        if self.score.lost > MAX_LOST:
            self.end_game()
            return

        self.root.after(FRAME_DELAY, self.update)

    def end_game(self):
        self.game_over = True
        self.canvas.create_text(
            WINDOW_WIDTH // 2,
            WINDOW_HEIGHT // 2 - 20,
            text="Гра завершена!",
            font=("Helvetica", 28, "bold"),
            fill="red",
        )
        self.canvas.create_text(
            WINDOW_WIDTH // 2,
            WINDOW_HEIGHT // 2 + 25,
            text=f"Ви пропустили {self.score.lost} яєць.",
            font=("Helvetica", 20),
            fill="red",
        )

    def run(self):
        self.update()
        self.root.mainloop()


if __name__ == "__main__":
    game = EggCatcherGame()
    game.run()

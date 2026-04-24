import random

from config import SCREEN_HEIGHT, SCREEN_WIDTH


class Target:
    def __init__(self, canvas, radius, color):
        self.canvas = canvas
        self.radius = radius
        self.id = None
        self.create(color)

    def create(self, color):
        x = random.randint(self.radius, SCREEN_WIDTH - self.radius)
        y = random.randint(self.radius, SCREEN_HEIGHT - self.radius)
        self.id = self.canvas.create_oval(
            x - self.radius,
            y - self.radius,
            x + self.radius,
            y + self.radius,
            fill=color,
            outline=color,
        )

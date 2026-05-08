import random

from base_entity import BaseEntity
from config import CRYSTAL_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH


class Crystal(BaseEntity):
    def __init__(self, canvas):
        size = CRYSTAL_SIZE
        x = random.randint(size * 2, SCREEN_WIDTH - size * 2)
        y = random.randint(80, SCREEN_HEIGHT - size * 4)
        item_id = canvas.create_polygon(
            x,
            y - size,
            x + size,
            y,
            x,
            y + size,
            x - size,
            y,
            fill="#ffd166",
            outline="#ffe5a4",
            width=2,
        )
        super().__init__(canvas, item_id)

    def get_coords(self):
        points = self.canvas.coords(self.item_id)
        xs = points[::2]
        ys = points[1::2]
        return min(xs), min(ys), max(xs), max(ys)

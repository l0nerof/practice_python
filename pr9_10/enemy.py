import random

from base_entity import BaseEntity
from config import ENEMY_BASE_SPEED, ENEMY_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH


class Enemy(BaseEntity):
    def __init__(self, canvas, level):
        spawn_side = random.choice(["top", "left", "right"])
        size = ENEMY_SIZE

        if spawn_side == "top":
            x = random.randint(size, SCREEN_WIDTH - size)
            y = -size * 2
        elif spawn_side == "left":
            x = -size * 2
            y = random.randint(60, SCREEN_HEIGHT - size)
        else:
            x = SCREEN_WIDTH + size * 2
            y = random.randint(60, SCREEN_HEIGHT - size)

        item_id = canvas.create_oval(
            x - size,
            y - size,
            x + size,
            y + size,
            fill="#ff5d73",
            outline="#ffc0c9",
            width=2,
        )
        super().__init__(canvas, item_id)
        self.speed = ENEMY_BASE_SPEED + (level - 1) * 0.25

    def update(self, target_x, target_y):
        current_x, current_y = self.get_center()
        dx = target_x - current_x
        dy = target_y - current_y
        distance = max((dx ** 2 + dy ** 2) ** 0.5, 1)

        self.canvas.move(
            self.item_id,
            dx / distance * self.speed,
            dy / distance * self.speed,
        )

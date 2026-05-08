from base_entity import BaseEntity
from config import PROJECTILE_SIZE, PROJECTILE_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH


class Projectile(BaseEntity):
    def __init__(self, canvas, start_x, start_y, target_x, target_y):
        radius = PROJECTILE_SIZE
        item_id = canvas.create_oval(
            start_x - radius,
            start_y - radius,
            start_x + radius,
            start_y + radius,
            fill="#ffffff",
            outline="#e8f6ff",
        )
        super().__init__(canvas, item_id)

        dx = target_x - start_x
        dy = target_y - start_y
        distance = max((dx ** 2 + dy ** 2) ** 0.5, 1)
        self.vx = dx / distance * PROJECTILE_SPEED
        self.vy = dy / distance * PROJECTILE_SPEED

    def update(self):
        self.canvas.move(self.item_id, self.vx, self.vy)

    def is_offscreen(self):
        x1, y1, x2, y2 = self.get_coords()
        return x2 < 0 or x1 > SCREEN_WIDTH or y2 < 0 or y1 > SCREEN_HEIGHT

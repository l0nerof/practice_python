from config import PLAYER_SIZE, PLAYER_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH
from base_entity import BaseEntity


class Player(BaseEntity):
    def __init__(self, canvas):
        half = PLAYER_SIZE
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT - 80
        item_id = canvas.create_rectangle(
            center_x - half,
            center_y - half,
            center_x + half,
            center_y + half,
            fill="#49d6ff",
            outline="#9bf0ff",
            width=2,
        )
        super().__init__(canvas, item_id)
        self.speed = PLAYER_SPEED
        self.dx = 0
        self.dy = 0
        self.invulnerability_frames = 0

    def set_direction(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def update(self):
        self.canvas.move(self.item_id, self.dx * self.speed, self.dy * self.speed)
        x1, y1, x2, y2 = self.get_coords()

        if x1 < 0:
            self.canvas.move(self.item_id, -x1, 0)
        elif x2 > SCREEN_WIDTH:
            self.canvas.move(self.item_id, SCREEN_WIDTH - x2, 0)

        if y1 < 50:
            self.canvas.move(self.item_id, 0, 50 - y1)
        elif y2 > SCREEN_HEIGHT:
            self.canvas.move(self.item_id, 0, SCREEN_HEIGHT - y2)

        if self.invulnerability_frames > 0:
            self.invulnerability_frames -= 1
            fill = "#1f6d80" if self.invulnerability_frames % 8 < 4 else "#49d6ff"
            self.canvas.itemconfig(self.item_id, fill=fill)
        else:
            self.canvas.itemconfig(self.item_id, fill="#49d6ff")

    def make_invulnerable(self, frames=45):
        self.invulnerability_frames = frames

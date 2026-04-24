from config import PLAYER_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH


class Player:
    def __init__(self, canvas, x, y, width, height, color):
        self.canvas = canvas
        self.vx = 0
        self.vy = 0
        self.id = canvas.create_rectangle(
            x,
            y,
            x + width,
            y + height,
            fill=color,
            outline=color,
        )

    def move_left(self, _event=None):
        self.vx = -PLAYER_SPEED

    def move_right(self, _event=None):
        self.vx = PLAYER_SPEED

    def move_up(self, _event=None):
        self.vy = -PLAYER_SPEED

    def move_down(self, _event=None):
        self.vy = PLAYER_SPEED

    def stop_horizontal(self, _event=None):
        self.vx = 0

    def stop_vertical(self, _event=None):
        self.vy = 0

    def move(self):
        self.canvas.move(self.id, self.vx, self.vy)
        left, top, right, bottom = self.canvas.coords(self.id)

        if left < 0:
            self.canvas.move(self.id, -left, 0)
        elif right > SCREEN_WIDTH:
            self.canvas.move(self.id, SCREEN_WIDTH - right, 0)

        if top < 0:
            self.canvas.move(self.id, 0, -top)
        elif bottom > SCREEN_HEIGHT:
            self.canvas.move(self.id, 0, SCREEN_HEIGHT - bottom)

    def collides_with(self, sprite_id):
        player_coords = self.canvas.coords(self.id)
        overlaps = self.canvas.find_overlapping(*player_coords)
        return sprite_id in overlaps

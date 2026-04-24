class Catcher:
    def __init__(self, canvas, color, score):
        self.canvas = canvas
        self.color = color
        self.score = score
        self.speed = 0
        self.width = 90
        self.height = 16
        self.canvas_width = int(self.canvas["width"])
        self.canvas_height = int(self.canvas["height"])

        start_x = self.canvas_width // 2
        y = self.canvas_height - 30

        self.id = self.canvas.create_rectangle(
            start_x - self.width // 2,
            y - self.height // 2,
            start_x + self.width // 2,
            y + self.height // 2,
            fill=self.color,
            outline=self.color,
        )

        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyRelease-Left>", self.stop_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
        self.canvas.bind_all("<KeyRelease-Right>", self.stop_right)

    def turn_left(self, _event):
        self.speed = -18

    def stop_left(self, _event):
        if self.speed < 0:
            self.speed = 0

    def turn_right(self, _event):
        self.speed = 18

    def stop_right(self, _event):
        if self.speed > 0:
            self.speed = 0

    def draw(self):
        self.canvas.move(self.id, self.speed, 0)
        left, _, right, _ = self.canvas.coords(self.id)

        if left < 0:
            self.canvas.move(self.id, -left, 0)
            self.speed = 0
        elif right > self.canvas_width:
            self.canvas.move(self.id, self.canvas_width - right, 0)
            self.speed = 0

    def catch(self, eggs):
        catcher_left, catcher_top, catcher_right, catcher_bottom = self.canvas.coords(self.id)

        for egg in list(eggs):
            egg_left, egg_top, egg_right, egg_bottom = self.canvas.coords(egg.id)

            horizontal_hit = egg_right >= catcher_left and egg_left <= catcher_right
            vertical_hit = egg_bottom >= catcher_top and egg_top <= catcher_bottom

            if horizontal_hit and vertical_hit:
                egg.delete()
                eggs.remove(egg)
                self.score.caught_egg()

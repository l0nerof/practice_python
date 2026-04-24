import random


class Egg:
    def __init__(self, canvas, color, score):
        self.canvas = canvas
        self.color = color
        self.score = score
        self.canvas_width = int(self.canvas["width"])
        self.canvas_height = int(self.canvas["height"])
        self.speed = random.randint(6, 12)

        x = random.randint(20, self.canvas_width - 20)
        self.id = self.canvas.create_oval(
            x - 12,
            0,
            x + 12,
            28,
            fill=self.color,
            outline="gray20",
            width=2,
        )

    def draw(self):
        self.canvas.move(self.id, 0, self.speed)
        _, _, _, bottom = self.canvas.coords(self.id)

        if bottom >= self.canvas_height:
            self.delete()
            self.score.lost_egg()
            return True

        return False

    def delete(self):
        self.canvas.delete(self.id)

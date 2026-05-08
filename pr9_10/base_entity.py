class BaseEntity:
    def __init__(self, canvas, item_id):
        self.canvas = canvas
        self.item_id = item_id

    def get_coords(self):
        return self.canvas.coords(self.item_id)

    def get_center(self):
        x1, y1, x2, y2 = self.get_coords()
        return (x1 + x2) / 2, (y1 + y2) / 2

    def intersects(self, other):
        ax1, ay1, ax2, ay2 = self.get_coords()
        bx1, by1, bx2, by2 = other.get_coords()

        return ax1 <= bx2 and ax2 >= bx1 and ay1 <= by2 and ay2 >= by1

    def delete(self):
        self.canvas.delete(self.item_id)

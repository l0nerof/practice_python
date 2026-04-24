class Score:
    def __init__(self, canvas):
        self.canvas = canvas
        self.caught = 0
        self.lost = 0
        self.text_id = None
        self.show_text()

    def show_text(self):
        text = f"Спіймав: {self.caught} Пропустив: {self.lost}"

        if self.text_id is None:
            self.text_id = self.canvas.create_text(
                250,
                25,
                text=text,
                font=("Helvetica", 18, "bold"),
                fill="black",
            )
        else:
            self.canvas.itemconfig(self.text_id, text=text)

    def caught_egg(self):
        self.caught += 1
        self.show_text()

    def lost_egg(self):
        self.lost += 1
        self.show_text()

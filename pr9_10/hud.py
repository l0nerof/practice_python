from config import ACCENT_COLOR, TEXT_COLOR


class Hud:
    def __init__(self, canvas):
        self.canvas = canvas
        self.info_id = canvas.create_text(
            12,
            12,
            anchor="nw",
            text="",
            fill=TEXT_COLOR,
            font=("Helvetica", 16, "bold"),
        )
        self.message_id = canvas.create_text(
            400,
            300,
            text="",
            fill=ACCENT_COLOR,
            font=("Helvetica", 28, "bold"),
        )
        self.submessage_id = canvas.create_text(
            400,
            345,
            text="",
            fill=TEXT_COLOR,
            font=("Helvetica", 14),
        )

    def update(self, score, lives, level):
        self.canvas.itemconfig(
            self.info_id,
            text=f"Очки: {score}   Життя: {lives}   Рівень: {level}",
        )

    def show_message(self, title, subtitle):
        self.canvas.itemconfig(self.message_id, text=title)
        self.canvas.itemconfig(self.submessage_id, text=subtitle)

    def clear_message(self):
        self.canvas.itemconfig(self.message_id, text="")
        self.canvas.itemconfig(self.submessage_id, text="")

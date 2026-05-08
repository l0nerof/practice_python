import random
import tkinter as tk

from config import (
    BACKGROUND_COLOR,
    CRYSTAL_SPAWN_FRAMES,
    ENEMY_SPAWN_FRAMES,
    FRAME_DELAY,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TEXT_COLOR,
    WINDOW_TITLE,
    WIN_SCORE,
)
from crystal import Crystal
from enemy import Enemy
from hud import Hud
from player import Player
from projectile import Projectile


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        self.root.resizable(False, False)
        self.root.wm_attributes("-topmost", 1)

        self.canvas = tk.Canvas(
            self.root,
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            bg=BACKGROUND_COLOR,
            bd=0,
            highlightthickness=0,
        )
        self.canvas.pack()

        self._draw_background()

        self.player = Player(self.canvas)
        self.hud = Hud(self.canvas)
        self.enemies = []
        self.projectiles = []
        self.crystals = []
        self.pressed_keys = set()

        self.score = 0
        self.lives = 3
        self.level = 1
        self.frame_count = 0
        self.running = True
        self.finished = False

        self.hud.update(self.score, self.lives, self.level)
        self.hud.show_message(
            "Crystal Sprint",
            "WASD / стрілки - рух, клік мишкою - постріл",
        )

        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.bind("<KeyRelease>", self.on_key_release)
        self.root.bind("<Button-1>", self.on_mouse_click)
        self.root.bind("<Escape>", self.on_escape)
        self.root.bind("<space>", self.on_space)

    def _draw_background(self):
        for _ in range(80):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            size = random.randint(1, 3)
            self.canvas.create_oval(
                x,
                y,
                x + size,
                y + size,
                fill="#22345d",
                outline="#22345d",
            )

        self.canvas.create_text(
            SCREEN_WIDTH // 2,
            24,
            text="Збирай кристали та знищуй ворогів",
            fill=TEXT_COLOR,
            font=("Helvetica", 14),
        )

    def on_key_press(self, event):
        self.pressed_keys.add(event.keysym.lower())

    def on_key_release(self, event):
        self.pressed_keys.discard(event.keysym.lower())

    def on_mouse_click(self, event):
        if self.finished:
            self.restart()
            return

        player_x, player_y = self.player.get_center()
        projectile = Projectile(self.canvas, player_x, player_y, event.x, event.y)
        self.projectiles.append(projectile)
        self.hud.clear_message()

    def on_escape(self, _event=None):
        self.running = False
        self.root.destroy()

    def on_space(self, _event=None):
        if self.finished:
            self.restart()

    def restart(self):
        self.root.destroy()
        new_game = Game()
        new_game.run()

    def update_player_direction(self):
        dx = 0
        dy = 0

        if "a" in self.pressed_keys or "left" in self.pressed_keys:
            dx -= 1
        if "d" in self.pressed_keys or "right" in self.pressed_keys:
            dx += 1
        if "w" in self.pressed_keys or "up" in self.pressed_keys:
            dy -= 1
        if "s" in self.pressed_keys or "down" in self.pressed_keys:
            dy += 1

        self.player.set_direction(dx, dy)

    def spawn_objects(self):
        if self.frame_count % max(25, ENEMY_SPAWN_FRAMES - self.level * 4) == 0:
            self.enemies.append(Enemy(self.canvas, self.level))

        if self.frame_count % CRYSTAL_SPAWN_FRAMES == 0 and len(self.crystals) < 3:
            self.crystals.append(Crystal(self.canvas))

    def update_projectiles(self):
        for projectile in list(self.projectiles):
            projectile.update()
            if projectile.is_offscreen():
                projectile.delete()
                self.projectiles.remove(projectile)

    def update_enemies(self):
        target_x, target_y = self.player.get_center()
        for enemy in self.enemies:
            enemy.update(target_x, target_y)

    def collect_crystals(self):
        for crystal in list(self.crystals):
            if self.player.intersects(crystal):
                crystal.delete()
                self.crystals.remove(crystal)
                self.score += 1

    def resolve_projectile_hits(self):
        for projectile in list(self.projectiles):
            for enemy in list(self.enemies):
                if projectile.intersects(enemy):
                    projectile.delete()
                    enemy.delete()
                    self.projectiles.remove(projectile)
                    self.enemies.remove(enemy)
                    self.score += 2
                    break

    def resolve_enemy_hits(self):
        if self.player.invulnerability_frames > 0:
            return

        for enemy in list(self.enemies):
            if self.player.intersects(enemy):
                enemy.delete()
                self.enemies.remove(enemy)
                self.lives -= 1
                self.player.make_invulnerable()
                break

    def update_level(self):
        self.level = 1 + self.score // 7

    def check_end_conditions(self):
        if self.score >= WIN_SCORE:
            self.finished = True
            self.running = False
            self.hud.show_message(
                "Перемога!",
                "Ти набрав достатньо очок. Клік мишкою або Space - перезапуск",
            )
            return

        if self.lives <= 0:
            self.finished = True
            self.running = False
            self.hud.show_message(
                "Поразка!",
                "Життя закінчились. Клік мишкою або Space - перезапуск",
            )

    def game_loop(self):
        if not self.running:
            return

        self.frame_count += 1
        self.update_player_direction()
        self.player.update()
        self.spawn_objects()
        self.update_projectiles()
        self.update_enemies()
        self.collect_crystals()
        self.resolve_projectile_hits()
        self.resolve_enemy_hits()
        self.update_level()
        self.hud.update(self.score, self.lives, self.level)
        self.check_end_conditions()

        if self.running:
            self.root.after(FRAME_DELAY, self.game_loop)

    def run(self):
        self.root.after(700, self.hud.clear_message)
        self.game_loop()
        self.root.mainloop()

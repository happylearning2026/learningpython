"""
贪吃蛇 —— pygame 版（macOS / Windows / Linux 通用）
安装依赖: pip install pygame
运行方式: python3 snake_game.py
操作方式: 方向键 / WASD 移动，空格暂停，R 重新开始
"""

import pygame
import random
import math
import sys

# ── 配置 ──────────────────────────────────────────────────────────────────────
COLS, ROWS  = 25, 25
CELL        = 24
WIDTH       = COLS * CELL          # 600
HEIGHT      = ROWS * CELL          # 600
HUD_HEIGHT  = 64
WIN_W       = WIDTH
WIN_H       = HEIGHT + HUD_HEIGHT
FPS         = 60
MOVE_INIT   = 0.15   # 初始移动间隔（秒）

# 配色
C_BG        = (10,  10,  15)
C_GRID      = (17,  17,  32)
C_HEAD      = (0,   255, 157)
C_BODY      = [(0, 204, 122), (0, 170, 102), (0, 136,  85), (0, 100,  68)]
C_FOOD      = (255,  45, 107)
C_BONUS     = (255, 225,  77)
C_TEXT      = (224, 255, 232)
C_DIM       = (42,  42,  58)
C_BORDER    = (0,   255, 157)

DIRS = {
    "UP":    (0, -1),
    "DOWN":  (0,  1),
    "LEFT":  (-1, 0),
    "RIGHT": (1,  0),
}
OPPOSITE = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}


# ── 粒子 ──────────────────────────────────────────────────────────────────────
class Particle:
    def __init__(self, x, y, color):
        angle = random.uniform(0, math.tau)
        speed = random.uniform(1.5, 4.5)
        self.x  = float(x)
        self.y  = float(y)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.life  = 1.0
        self.decay = random.uniform(0.03, 0.07)
        self.size  = random.uniform(2, 5)
        self.color = color

    def update(self):
        self.x  += self.vx
        self.y  += self.vy
        self.vy += 0.12
        self.life -= self.decay

    @property
    def alive(self):
        return self.life > 0


# ── 工具函数 ──────────────────────────────────────────────────────────────────
def lerp_color(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def draw_rounded_rect(surf, color, rect, radius):
    x, y, w, h = rect
    r = min(radius, w // 2, h // 2)
    pygame.draw.rect(surf, color, (x + r, y, w - 2*r, h))
    pygame.draw.rect(surf, color, (x, y + r, w, h - 2*r))
    for cx, cy in [(x+r, y+r), (x+w-r, y+r), (x+r, y+h-r), (x+w-r, y+h-r)]:
        pygame.draw.circle(surf, color, (cx, cy), r)


def glow_circle(surf, color, center, radius, layers=4):
    for i in range(layers, 0, -1):
        alpha = int(60 * (i / layers))
        r_exp = radius + i * 3
        s = pygame.Surface((r_exp*2+2, r_exp*2+2), pygame.SRCALPHA)
        pygame.draw.circle(s, (*color, alpha), (r_exp+1, r_exp+1), r_exp)
        surf.blit(s, (center[0]-r_exp-1, center[1]-r_exp-1))
    pygame.draw.circle(surf, color, center, radius)


# ── 游戏类 ────────────────────────────────────────────────────────────────────
class SnakeGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake  贪吃蛇")
        self.screen = pygame.display.set_mode((WIN_W, WIN_H))
        self.clock  = pygame.time.Clock()
        self._load_fonts()
        self.best = 0
        self._new_game()
        self._state = "menu"

    def _load_fonts(self):
        for name in ["Courier New", "Menlo", "Monaco", "Courier"]:
            try:
                self.font_big   = pygame.font.SysFont(name, 30, bold=True)
                self.font_mid   = pygame.font.SysFont(name, 20, bold=True)
                self.font_small = pygame.font.SysFont(name, 13)
                return
            except Exception:
                continue
        self.font_big   = pygame.font.Font(None, 36)
        self.font_mid   = pygame.font.Font(None, 24)
        self.font_small = pygame.font.Font(None, 16)

    def _new_game(self):
        mid = COLS // 2
        self.snake         = [(mid, ROWS//2), (mid-1, ROWS//2), (mid-2, ROWS//2)]
        self.direction     = "RIGHT"
        self.next_dir      = "RIGHT"
        self.score         = 0
        self.level         = 1
        self.move_interval = MOVE_INIT
        self.move_timer    = 0.0
        self.particles     = []
        self.bonus         = None
        self.bonus_life    = 0
        self.shake         = 0
        self.eat_flash     = 0
        self._spawn_food()

    def _spawn_food(self):
        occupied = set(self.snake)
        while True:
            p = (random.randint(0, COLS-1), random.randint(0, ROWS-1))
            if p not in occupied:
                self.food = p
                return

    def _spawn_bonus(self):
        occupied = set(self.snake) | {self.food}
        for _ in range(200):
            p = (random.randint(0, COLS-1), random.randint(0, ROWS-1))
            if p not in occupied:
                self.bonus      = p
                self.bonus_life = 90
                return

    # ── 主循环 ────────────────────────────────────────────────────────────────
    def run(self):
        while True:
            dt = self.clock.tick(FPS) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self._handle_event(event)
            self._update(dt)
            self._draw()
            pygame.display.flip()

    def _handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        key = event.key
        dir_map = {
            pygame.K_UP: "UP",    pygame.K_w: "UP",
            pygame.K_DOWN: "DOWN", pygame.K_s: "DOWN",
            pygame.K_LEFT: "LEFT", pygame.K_a: "LEFT",
            pygame.K_RIGHT: "RIGHT", pygame.K_d: "RIGHT",
        }
        if key in dir_map and self._state == "playing":
            nd = dir_map[key]
            if nd != OPPOSITE[self.direction]:
                self.next_dir = nd

        if key in (pygame.K_SPACE, pygame.K_RETURN):
            if self._state == "menu":
                self._state = "playing"
            elif self._state == "playing":
                self._state = "paused"
            elif self._state == "paused":
                self._state = "playing"
            elif self._state == "gameover":
                self._new_game()
                self._state = "playing"

        if key == pygame.K_r:
            self._new_game()
            self._state = "playing"

    def _update(self, dt):
        # 粒子和震屏在任何状态都继续
        self.particles = [p for p in self.particles if p.alive]
        for p in self.particles:
            p.update()
        if self.shake > 0:
            self.shake -= 1
        if self.eat_flash > 0:
            self.eat_flash -= 1

        if self._state != "playing":
            return

        self.move_timer += dt
        if self.move_timer >= self.move_interval:
            self.move_timer -= self.move_interval
            self._step()

    def _step(self):
        self.direction = self.next_dir
        dx, dy = DIRS[self.direction]
        hx, hy = self.snake[0]
        nx, ny = hx + dx, hy + dy

        if not (0 <= nx < COLS and 0 <= ny < ROWS):
            return self._game_over()
        if (nx, ny) in self.snake:
            return self._game_over()

        self.snake.insert(0, (nx, ny))
        grew = False

        if (nx, ny) == self.food:
            grew = True
            self.score += self.level * 10
            self.shake     = 5
            self.eat_flash = 8
            self._burst((nx+.5)*CELL, (ny+.5)*CELL, C_FOOD, 14)
            self._spawn_food()
            if self.score % 50 == 0 and not self.bonus:
                self._spawn_bonus()
            self._level_up()

        if self.bonus and (nx, ny) == self.bonus:
            grew = True
            self.score += self.level * 30
            self._burst((nx+.5)*CELL, (ny+.5)*CELL, C_BONUS, 22)
            self.bonus = None

        if not grew:
            self.snake.pop()

        if self.bonus:
            self.bonus_life -= 1
            if self.bonus_life <= 0:
                self.bonus = None

        if self.score > self.best:
            self.best = self.score

    def _level_up(self):
        new_level = self.score // 100 + 1
        if new_level > self.level:
            self.level = new_level
            self.move_interval = max(0.055, MOVE_INIT - (self.level-1) * 0.012)

    def _game_over(self):
        self._burst(
            (self.snake[0][0]+.5)*CELL,
            (self.snake[0][1]+.5)*CELL,
            C_FOOD, 30,
        )
        self.shake  = 12
        self._state = "gameover"

    def _burst(self, x, y, color, n):
        for _ in range(n):
            self.particles.append(Particle(x, y, color))

    # ── 绘制 ──────────────────────────────────────────────────────────────────
    def _draw(self):
        self.screen.fill(C_BG)
        self._draw_hud()

        ox = oy = 0
        if self.shake > 0:
            ox = random.randint(-3, 3)
            oy = random.randint(-3, 3)

        # 游戏区 surface
        game_surf = pygame.Surface((WIDTH, HEIGHT))
        game_surf.fill(C_BG)
        self._draw_grid(game_surf)
        self._draw_food_obj(game_surf)
        if self.bonus:
            self._draw_bonus_obj(game_surf)
        self._draw_snake_obj(game_surf)
        self._draw_particles(game_surf)

        self.screen.blit(game_surf, (ox, HUD_HEIGHT + oy))
        pygame.draw.rect(self.screen, C_BORDER,
                         (ox, HUD_HEIGHT+oy, WIDTH, HEIGHT), 2)

        if self._state == "menu":
            self._draw_overlay("贪  吃  蛇", "", "按 Enter 或 空格 开始")
        elif self._state == "paused":
            self._draw_overlay("已  暂  停", "", "空格继续 | R 重新开始")
        elif self._state == "gameover":
            self._draw_overlay("游 戏 结 束",
                               f"得分：{self.score}",
                               "Enter / 空格 / R  重新开始")

    def _draw_hud(self):
        pygame.draw.line(self.screen, C_DIM, (0, HUD_HEIGHT-1), (WIN_W, HUD_HEIGHT-1))
        items = [("分  数", self.score), ("最高分", self.best), ("等  级", self.level)]
        spacing = WIN_W // len(items)
        for i, (label, val) in enumerate(items):
            cx = spacing * i + spacing // 2
            lbl_s = self.font_small.render(label, True, C_DIM)
            val_s = self.font_big.render(str(val), True, C_HEAD)
            self.screen.blit(lbl_s, lbl_s.get_rect(center=(cx, 16)))
            self.screen.blit(val_s, val_s.get_rect(center=(cx, 44)))

    def _draw_grid(self, surf):
        for r in range(ROWS):
            for c in range(COLS):
                cx = c * CELL + CELL // 2
                cy = r * CELL + CELL // 2
                pygame.draw.rect(surf, C_GRID, (cx, cy, 1, 1))

    def _draw_food_obj(self, surf):
        t     = pygame.time.get_ticks() / 400
        pulse = 0.85 + math.sin(t) * 0.15
        fx, fy = self.food
        cx = int((fx + .5) * CELL)
        cy = int((fy + .5) * CELL)
        r  = int(CELL * 0.35 * pulse)
        glow_circle(surf, C_FOOD, (cx, cy), r, layers=3)
        pygame.draw.circle(surf, (255, 180, 200),
                           (cx - r//3, cy - r//3), max(1, r//3))

    def _draw_bonus_obj(self, surf):
        bx, by = self.bonus
        cx = int((bx + .5) * CELL)
        cy = int((by + .5) * CELL)
        t  = pygame.time.get_ticks() / 200
        pulse = 0.85 + math.sin(t) * 0.15
        r  = int(CELL * 0.38 * pulse)
        alpha = int(255 * min(1.0, self.bonus_life / 30))
        s = pygame.Surface((CELL*2, CELL*2), pygame.SRCALPHA)
        pts = []
        for i in range(10):
            angle = math.pi * i / 5 - math.pi / 2
            rad   = r if i % 2 == 0 else r * 0.45
            pts.append((CELL + math.cos(angle)*rad, CELL + math.sin(angle)*rad))
        pygame.draw.polygon(s, (*C_BONUS, alpha), pts)
        surf.blit(s, (cx - CELL, cy - CELL))

    def _draw_snake_obj(self, surf):
        length = len(self.snake)
        for i, (sx, sy) in enumerate(reversed(self.snake)):
            real_i = length - 1 - i
            t = real_i / max(length - 1, 1)
            x = sx * CELL + 2
            y = sy * CELL + 2
            sz = CELL - 4

            if real_i == 0:
                if self.eat_flash > 0:
                    glow_r = CELL
                    gs = pygame.Surface((glow_r*4, glow_r*4), pygame.SRCALPHA)
                    pygame.draw.circle(gs, (*C_HEAD, 50),
                                       (glow_r*2, glow_r*2), glow_r*2)
                    surf.blit(gs, (sx*CELL + CELL//2 - glow_r*2,
                                   sy*CELL + CELL//2 - glow_r*2))
                color = C_HEAD
            else:
                idx = min(int(t * len(C_BODY)), len(C_BODY)-1)
                color = C_BODY[idx]
                if t > 0.6:
                    fade = (t - 0.6) / 0.4
                    color = lerp_color(color, C_BG, fade * 0.5)

            draw_rounded_rect(surf, color, (x, y, sz, sz), CELL//4)
            if real_i == 0:
                self._draw_eyes(surf, sx, sy)

    def _draw_eyes(self, surf, sx, sy):
        cx = (sx + .5) * CELL
        cy = (sy + .5) * CELL
        r  = max(2, int(CELL * 0.09))
        d  = CELL * 0.22
        fw = CELL * 0.15
        eye_positions = {
            "RIGHT": [(cx+fw, cy-d), (cx+fw, cy+d)],
            "LEFT":  [(cx-fw, cy-d), (cx-fw, cy+d)],
            "UP":    [(cx-d, cy-fw), (cx+d, cy-fw)],
            "DOWN":  [(cx-d, cy+fw), (cx+d, cy+fw)],
        }
        for ex, ey in eye_positions[self.direction]:
            pygame.draw.circle(surf, C_BG, (int(ex), int(ey)), r)
            pygame.draw.circle(surf, (255, 255, 255),
                               (int(ex + r*0.3), int(ey - r*0.2)), max(1, r//2))

    def _draw_particles(self, surf):
        for p in self.particles:
            if not p.alive:
                continue
            sz = max(1, int(p.size * p.life))
            alpha = int(p.life * 220)
            s = pygame.Surface((sz*2+1, sz*2+1), pygame.SRCALPHA)
            pygame.draw.rect(s, (*p.color, alpha), (0, 0, sz*2+1, sz*2+1))
            surf.blit(s, (int(p.x) - sz, int(p.y) - sz))

    def _draw_overlay(self, title, subtitle, hint):
        overlay = pygame.Surface((WIN_W, WIN_H), pygame.SRCALPHA)
        overlay.fill((10, 10, 15, 185))
        self.screen.blit(overlay, (0, 0))

        card_w, card_h = 360, 160
        card_x = (WIN_W - card_w) // 2
        card_y = (WIN_H - card_h) // 2
        card = pygame.Surface((card_w, card_h), pygame.SRCALPHA)
        card.fill((13, 13, 32, 230))
        self.screen.blit(card, (card_x, card_y))
        pygame.draw.rect(self.screen, C_HEAD,
                         (card_x, card_y, card_w, card_h), 2)

        title_s = self.font_big.render(title, True, C_FOOD)
        self.screen.blit(title_s, title_s.get_rect(center=(WIN_W//2, card_y + 40)))

        if subtitle:
            sub_s = self.font_mid.render(subtitle, True, C_BONUS)
            self.screen.blit(sub_s, sub_s.get_rect(center=(WIN_W//2, card_y + 82)))

        hint_s = self.font_small.render(hint, True, C_DIM)
        self.screen.blit(hint_s, hint_s.get_rect(center=(WIN_W//2, card_y + card_h - 22)))


# ── 入口 ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    SnakeGame().run()
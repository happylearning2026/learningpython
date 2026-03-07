import sys
import random
import pygame

CELL = 20
GRID_W, GRID_H = 20, 20
WIDTH, HEIGHT = CELL * GRID_W, CELL * GRID_H
FPS = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (40, 40, 40)

def random_food(snake):
    while True:
        p = (random.randrange(GRID_W), random.randrange(GRID_H))
        if p not in snake:
            return p

def draw_text(surf, text, size, x, y, color=WHITE):
    font = pygame.font.SysFont(None, size)
    img = font.render(text, True, color)
    surf.blit(img, (x, y))

def play():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("贪吃蛇")
    clock = pygame.time.Clock()

    def reset():
        mid = (GRID_W // 2, GRID_H // 2)
        snake = [mid, (mid[0]-1, mid[1]), (mid[0]-2, mid[1])]
        direction = (1, 0)
        food = random_food(snake)
        score = 0
        return snake, direction, food, score, False

    snake, direction, food, score, game_over = reset()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w) and direction != (0, 1):
                    direction = (0, -1)
                elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != (0, -1):
                    direction = (0, 1)
                elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != (-1, 0):
                    direction = (1, 0)
                elif event.key == pygame.K_r and game_over:
                    snake, direction, food, score, game_over = reset()
                elif event.key in (pygame.K_ESCAPE, pygame.K_q):
                    pygame.quit(); sys.exit()

        if not game_over:
            head = snake[0]
            new_head = (head[0] + direction[0], head[1] + direction[1])

            # 边界碰撞 -> 游戏结束
            if not (0 <= new_head[0] < GRID_W and 0 <= new_head[1] < GRID_H):
                game_over = True
            # 自身碰撞
            elif new_head in snake:
                game_over = True
            else:
                snake.insert(0, new_head)
                if new_head == food:
                    score += 1
                    food = random_food(snake)
                else:
                    snake.pop()

        screen.fill(BLACK)
        # 网格（可选）
        for x in range(0, WIDTH, CELL):
            pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, CELL):
            pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

        # 食物
        fx, fy = food
        pygame.draw.rect(screen, RED, (fx*CELL, fy*CELL, CELL, CELL))

        # 蛇
        for i, (sx, sy) in enumerate(snake):
            color = GREEN if i == 0 else (0, 160, 0)
            pygame.draw.rect(screen, color, (sx*CELL, sy*CELL, CELL, CELL))

        draw_text(screen, f"得分: {score}", 24, 5, 5)
        if game_over:
            draw_text(screen, "游戏结束 - 按 R 重来  Q/ESC 退出", 28, 20, HEIGHT//2 - 20, WHITE)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    play()
import pygame
import random
import sys

# 初始化 pygame
pygame.init()

# 颜色定义 (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# 游戏参数
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
CELL_NUMBER_X = WINDOW_WIDTH // CELL_SIZE
CELL_NUMBER_Y = WINDOW_HEIGHT // CELL_SIZE

# 创建游戏窗口
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("🐍 贪吃蛇 - by Grok")
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.body = [pygame.Vector2(5, 10), pygame.Vector2(4, 10), pygame.Vector2(3, 10)]
        self.direction = pygame.Vector2(1, 0)  # 初始向右
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREEN, block_rect)

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def check_collision(self):
        # 撞墙
        if not 0 <= self.body[0].x < CELL_NUMBER_X or not 0 <= self.body[0].y < CELL_NUMBER_Y:
            return True
        
        # 撞自己
        for block in self.body[1:]:
            if block == self.body[0]:
                return True
        return False

class Food:
    def __init__(self):
        self.randomize()

    def draw_food(self):
        food_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, food_rect)

    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER_X - 1)
        self.y = random.randint(0, CELL_NUMBER_Y - 1)
        self.pos = pygame.Vector2(self.x, self.y)

def main():
    # 创建蛇和食物
    snake = Snake()
    food = Food()

    # 分数
    score = 0

    # 游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # 方向控制（防止反向）
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction.y != 1:
                    snake.direction = pygame.Vector2(0, -1)
                if event.key == pygame.K_DOWN and snake.direction.y != -1:
                    snake.direction = pygame.Vector2(0, 1)
                if event.key == pygame.K_RIGHT and snake.direction.x != -1:
                    snake.direction = pygame.Vector2(1, 0)
                if event.key == pygame.K_LEFT and snake.direction.x != 1:
                    snake.direction = pygame.Vector2(-1, 0)
                if event.key == pygame.K_r:  # R键重启
                    return main()

        # 更新蛇的位置
        snake.move_snake()
        
        # 检查吃食物
        if snake.body[0] == food.pos:
            snake.add_block()
            food.randomize()
            score += 10
            # 防止食物生成在蛇身上
            for block in snake.body[1:]:
                if block == food.pos:
                    food.randomize()

        # 检查碰撞
        if snake.check_collision():
            # 游戏结束画面
            screen.fill(BLACK)
            font = pygame.font.Font(None, 74)
            text = font.render(f"游戏结束! 分数: {score}", True, WHITE)
            text_rect = text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
            screen.blit(text, text_rect)
            
            small_font = pygame.font.Font(None, 36)
            restart_text = small_font.render("按 R 键重玩", True, YELLOW)
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 60))
            screen.blit(restart_text, restart_rect)
            
            pygame.display.update()
            continue

        # 绘制画面
        screen.fill(BLACK)
        snake.draw_snake()
        food.draw_food()

        # 显示分数
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"分数: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(12)  # 控制游戏速度（蛇移动频率）

if __name__ == "__main__":
    main()
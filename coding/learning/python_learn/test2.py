import pygame
import time
import random

# 初始化 pygame
pygame.init()

# 设置游戏窗口大小
width = 600
height = 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇游戏")

# 颜色定义
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 设置蛇的初始大小和速度
snake_block = 10
snake_speed = 10  # 修改为较慢的速度

# 字体设置
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# 显示分数
def Your_score(score):
    value = score_font.render("分数: " + str(score), True, black)
    win.blit(value, [0, 0])

# 绘制蛇
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, green, [x[0], x[1], snake_block, snake_block])

# 显示消息
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3])

# 游戏主函数
def gameLoop():
    game_over = False
    game_close = False

    # 蛇的初始位置
    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # 食物的随机位置
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not game_over:

        while game_close == True:
            win.fill(blue)
            message("游戏结束! 按Q退出 或 按C重新开始", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # 处理结束状态下的事件
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # 按Q退出游戏
                        game_over = True
                    if event.key == pygame.K_c:  # 按C重新开始
                        gameLoop()  # 递归调用重新开始游戏

        # 游戏事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 点击窗口的关闭按钮
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # 边界检查，碰壁游戏结束
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        win.fill(blue)

        # 绘制食物
        pygame.draw.rect(win, yellow, [foodx, foody, snake_block, snake_block])

        # 更新蛇的长度
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # 如果蛇撞到自己则游戏结束
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # 判断是否吃到食物
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# 启动游戏
gameLoop()
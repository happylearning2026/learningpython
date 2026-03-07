import random

def play():
    target = random.randint(1, 10)   # 缩小范围
    # max_tries = 3   # 不再需要

    while True:                       # 不限制次数
        try:
            guess = int(input("猜一个 1-10 之间的数字："))
        except ValueError:
            print("请输入整数。")

            continue

        if guess == target:
            print("恭喜，你猜对了！")
            break
        elif guess < target:
            print("太小了。")
        else:
            print("太大了。")

if __name__ == "__main__":
    play()
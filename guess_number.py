import random

answer = random.randint(1, 10)
is_correct = False

for attempt in range(1, 4):
    guess = int(input(f"第 {attempt} 次猜数字（1 到 10）："))

    if guess == answer:
        print("恭喜你，猜对了！")
        is_correct = True
        break
    elif guess > answer:
        print("猜大啦")
    else:
        print("猜小啦")

if not is_correct:
    print(f"三次机会用完了，正确答案是：{answer}")

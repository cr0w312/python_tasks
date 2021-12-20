num = int(input())
step = 0
if num % 2 == 0:
    while num % 2 == 0:
        num //= 2
        step += 1
    if num == 1:
        print(step)
    elif num != 1:
        print("НЕТ")
elif num == 1:
    print(step)
elif num % 2 != 0:
    print('НЕТ')
colvo = int(input())
steps = 0
while colvo != 1:
    if colvo % 2 == 0:
        colvo //= 2
        steps += 1
    elif colvo != 1:
        colvo -= 1
        steps += 1
print(steps)
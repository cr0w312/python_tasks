num = int(input())
colvo = 0
while num != 1:
    if num % 2 == 0:
        num = num // 2
    elif num % 2 != 0:
        num = num * 3 + 1
    colvo += 1
print(colvo)
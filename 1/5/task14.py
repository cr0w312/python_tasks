total1 = int(input())
total2 = int(input())
total3 = int(input())
num = 0
step = 0
while total1 != 0 or total2 != 0 or total3 != 0:
    num = int(input())
    step = int(input())
    if num == 1:
        total1 -= step
    elif num == 2:
        total2 -= step
    elif num == 3:
        total3 -= step
    print(total1, total2, total3)
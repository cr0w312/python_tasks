total1 = int(input())
total2 = int(input())
if total1 > total2:
    ii = total1 - total2
    total1 -= ii
    num = 1
elif total1 < total2:
    ii = total2 - total1
    total2 -= ii
    num = 2
elif total1 == total2:
    ii = 1
    total1 -= ii
    num = 1
print(num, ii, total1, total2)
while total1 != 0 or total2 != 0:
    num = int(input())
    user = int(input())
    n = 0
    u = 0
    while n == 0 or u == 0:
        n = 1
        u = 1
        if num != 1 and num != 2:
            n = 0
            print('Некорректный ход:', num, user)
            num = int(input())
            user = int(input())
        else:
            if num == 1:
                total = total1
            if num == 2:
                total = total2
            if user > total or user <= 0:
                u = 0
                print('Некорректный ход:', num, user)
                num = int(input())
                user = int(input())
    if num == 1:
        total1 -= user
    elif num == 2:
        total2 -= user
    print(num, user, total1, total2)
    if total1 == 0 and total2 == 0:
        print('Вы выиграли!')
        break

    if total1 > total2:
        ii = total1 - total2
        total1 -= ii
        num = 1
    elif total1 < total2:
        ii = total2 - total1
        total2 -= ii
        num = 2
    elif total1 == total2:
        ii = 1
        total1 -= ii
        num = 1
    print(num, ii, total1, total2)
    if total1 == 0 and total2 == 0:
        print('ИИ выиграл!')
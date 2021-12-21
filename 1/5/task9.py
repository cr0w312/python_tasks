total1 = int(input())
total2 = int(input())
total3 = int(input())
while total1 != 0 or total2 != 0 or total3 != 0:  # высч. хода прог.
    if total1 != 0 and total2 != 0 and total3 != 0:
        if total1 == total2 == total3: 
            num = 1
            ii = total1
            total1 -= ii
        elif total1 >= total2 >= total3:
            num = 1
            ii = total1 - total3
            total1 -= ii
        elif total1 >= total3 >= total2:
            num = 1
            ii = total1 - total2
            total1 -= ii
        elif total2 >= total1 >= total3:
            num = 2
            ii = total2 - total3
            total2 -= ii
        elif total2 >= total3 >= total1:
            num = 2
            ii = total2 - total1
            total2 -= ii
        elif total3 >= total1 >= total2:
            num = 3
            ii = total3 - total2
            total3 -= ii
        elif total3 >= total2 >= total1:
            num = 3
            ii = total3 - total1
            total3 -= ii
    elif total1 == 0:
        if total2 >= total3:
            num = 2
            ii = total2 - total3
            if ii == 0:
                ii = 1
            total2 -= ii
        elif total3 >= total2:
            num = 3
            ii = total3 - total2
            if ii == 0:
                ii = 1
            total3 -= ii
    elif total2 == 0:
        if total1 >= total3:
            num = 1
            ii = total1 - total3
            if ii == 0:
                ii = 1
            total1 -= ii
        elif total3 >= total1:
            num = 3
            ii = total3 - total1
            if ii == 0:
                ii = 1
            total3 -= ii
    elif total3 == 0:
        if total1 >= total2:
            num = 1
            ii = total1 - total2
            if ii == 0:
                ii = 1
            total1 -= ii
        elif total2 >= total1:
            num = 2
            ii = total2 - total1
            if ii == 0:
                ii = 1
            total2 -= ii
    print(num, ii, total1, total2, total3)
    if total1 == 0 and total2 == 0 and total3 == 0:
        print('ИИ выиграл!')
        break

    num = int(input())
    user = int(input())
    n = 0
    u = 0
    while n == 0 or u == 0:  # проверка кор хода
        n = 1
        u = 1
        if num != 1 and num != 2 and num != 3:
            n = 0
            print('Некорректный ход:', num, user)
            num = int(input())
            user = int(input())
        else:
            if num == 1:
                total = total1
            if num == 2:
                total = total2
            if num == 3:
                total = total3
            if user > total or user <= 0:
                u = 0
                print('Некорректный ход:', num, user)
                num = int(input())
                user = int(input())
    if num == 1:
        total1 -= user
    elif num == 2:
        total2 -= user
    elif num == 3:
        total3 -= user
    print(num, user, total1, total2, total3)
    if total1 == 0 and total2 == 0 and total3 == 0:
        print('Вы выиграли!')
        break

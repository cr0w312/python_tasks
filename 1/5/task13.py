total = int(input())
ii = 0
if 2 <= total <= 4:
    ii = total - 1
elif total == 1:
    ii = total
elif total >= 5:
    if 4 > total % 5 > 0:
        ii = total % 5
    else:
        ii = 1
total -= ii
print(ii, total)
if total == 0:
    print('Вы выиграли!')
while total != 0:
    user = int(input())
    while user > 3 or user > total or user <= 0:
        print('Некорректный ход:', user)
        user = int(input())
    total -= user
    print(user, total)
    if total == 0:
        print('ИИ выиграл!')
    else:
        if 2 <= total <= 4:
            ii = total - 1
        elif total == 1:
            ii = total
        elif total >= 5:
            if 4 > total % 5 > 0:
                ii = total % 5
            else:
                ii = 1
        total -= ii
        print(ii, total)
        if total == 0:
            print('Вы выиграли!')
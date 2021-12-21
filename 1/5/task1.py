stones = int(input())
if stones <= 3:
    ii = stones
elif stones >= 4:
    if stones % 4 == 0:
        ii = 1
    elif stones % 4 != 0:
        ii = stones % 4
stones -= ii 
print(ii, stones)
if stones == 0:
    print('ИИ выиграл!')
while stones != 0:
    hum = int(input())
    while hum > 3 or hum > stones or hum <= 0:
        print('Некорректный ход:', hum)
        hum = int(input())
    stones -= hum
    print(hum, stones)
    if stones == 0:
        print('Вы выиграли!')
        break
    else:
        if stones <= 3:
            ii = stones
        elif stones >= 4:
            if stones % 4 == 0:
                ii = 1
            elif stones % 4 != 0:
                ii = stones % 4
        stones -= ii
        print(ii, stones)
        if stones == 0:
            print('ИИ выиграл!')
            break
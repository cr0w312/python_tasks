ch = int(input())
sot = ch // 100
des = ch % 100 // 10
ed = ch % 10
if sot > des > ed or (ed > des > sot) or (ed == des == sot) and \
        ((sot + ed) / 2 == des):
    print('Вы ввели красивое число')
elif sot > ed > des or (des > ed > sot) or (des == ed == sot) and \
        ((sot + des) / 2 == ed):
    print('Вы ввели красивое число')
elif des > sot > ed or (ed > sot > des) or (ed == sot == des) and \
        ((des + ed) / 2 == sot):
    print('Вы ввели красивое число')
else:
    print('Жаль, вы ввели обычное число')

dlstr = 0
prost = 0
rasnc = 0
while dlstr == 0 or prost == 0 or rasnc == 0:
    dlstr = 1
    prost = 1
    rasnc = 1
    pas1 = input()
    pas2 = input()
    if len(pas1) < 8:
        print('Короткий!')
        dlstr = 0
    elif '123' in pas1:
        print('Простой!')
        prost = 0
    elif pas1 != pas2:
        print('Различаются.')
        rasnc = 0
if dlstr == 1 and prost == 1 and rasnc == 1:
    print('OK')
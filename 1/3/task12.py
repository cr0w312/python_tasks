god = int(input())
x4 = god % 4
x100 = god % 100
x400 = god % 400
if x400 == 0:
    print("Високосный")
elif x4 == 0 and x100 != 0:
    print("Високосный")
else:
    print("Не високосный")
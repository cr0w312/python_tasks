maxr = 0
minr = 190
rost = input()
colvo = 0
propusk = 0
while rost != "!":
    if 190 >= int(rost) >= 150:
        colvo = colvo + 1
        if int(rost) > maxr:
            maxr = int(rost)
        if int(rost) < minr:
            minr = int(rost)
    rost = input()
print(colvo)
print(minr, maxr)
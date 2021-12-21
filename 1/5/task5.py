colvo = int(input())
while colvo != 0:
    vsal = int(input())
    while vsal > 3 or vsal > colvo:
        print(colvo)
        vsal = int(input())
    colvo -= vsal
    print(colvo)
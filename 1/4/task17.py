rangstart = 0
rangfinish = 1000
rang = rangfinish - rangstart
prog = rangstart + (rang // 2)
print(prog)
user = input()
while user != '=':
    while user == '<':
        rangfinish = prog
        rang = rangfinish - rangstart
        prog = rangstart + (rang // 2)
        print(prog)
        user = input()
    while user == '>':
        rangstart = prog
        rang = rangfinish - rangstart
        prog = rangstart + (rang // 2)
        print(prog)
        user = input()
        
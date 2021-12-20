r1 = int(input())
r2 = int(input())
r3 = int(input())
if r1 >= r2 >= r3:
    print(r1)
    print(r2)
    print(r3)
elif r1 >= r3 >= r2:
    print(r1)
    print(r3)
    print(r2)
elif r2 >= r1 >= r3:
    print(r2)
    print(r1)
    print(r3)
elif r2 >= r3 >= r1:
    print(r2)
    print(r3)
    print(r1)
elif r3 >= r2 >= r1:
    print(r3)
    print(r2)
    print(r1)
elif r3 >= r1 >= r2:
    print(r3)
    print(r1)
    print(r2)
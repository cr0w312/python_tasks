d = int(input())
while d // 8 >= 1:
    d //= 8
print(d % 8)
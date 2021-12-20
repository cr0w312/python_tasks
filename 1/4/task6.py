sm = 0
ch = float((input)())
while ch >= 0:
    if ch > 1000:
        ch = ch * 0.95
    sm = sm + ch
    ch = float(input())
print(sm)
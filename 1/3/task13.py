ch = int(input())
t = ch // 1000
s = ch % 1000 // 100
d = ch % 1000 % 100 // 10
e = ch % 10
if t <= s <= d <= e:
    print(t * 1000 + s * 100 + d * 10 + e)
elif t <= s <= e <= d:
    print(t * 1000 + s * 100 + e * 10 + d)
elif t <= d <= s <= e:
    print(t * 1000 + d * 100 + s * 10 + e)
elif t <= d <= e <= s:
    print(t * 1000 + d * 100 + e * 10 + s)
elif t <= e <= s <= d:
    print(t * 1000 + e * 100 + s * 10 + d)
elif t <= e <= d <= s:
    print(t * 1000 + e * 100 + d * 10 + s)
elif s <= t <= d <= e:
    print(s * 1000 + t * 100 + d * 10 + e)
elif s <= t <= e <= d:
    print(s * 1000 + t * 100 + e * 10 + d)
elif s <= d <= t <= e:
    print(s * 1000 + d * 100 + t * 10 + e)
elif s <= d <= e <= t:
    print(s * 1000 + d * 100 + e * 10 + t)
elif s <= e <= d <= t:
    print(s * 1000 + e * 100 + d * 10 + t)
elif s <= e <= t <= d:
    print(s * 1000 + e * 100 + t * 10 + d)
elif d <= t <= s <= e:
    print(d * 1000 + t * 100 + s * 10 + e)
elif d <= t <= e <= s:
    print(d * 1000 + t * 100 + e * 10 + s)
elif d <= s <= t <= e:
    print(d * 1000 + s * 100 + t * 10 + e)
elif d <= s <= e <= t:
    print(d * 1000 + s * 100 + e * 10 + t)
elif d <= e <= t <= s:
    print(d * 1000 + e * 100 + t * 10 + s)
elif d <= e <= s <= t:
    print(d * 1000 + e * 100 + s * 10 + t)
elif e <= t <= s <= d:
    print(e * 1000 + t * 100 + s * 10 + d)   
elif e <= t <= d <= s:
    print(e * 1000 + t * 100 + d * 10 + s)
elif e <= s <= t <= d:
    print(e * 1000 + s * 100 + t * 10 + d)
elif e <= s <= d <= t:
    print(e * 1000 + s * 100 + d * 10 + t)
elif e <= d <= s <= t:
    print(e * 1000 + d * 100 + s * 10 + t)
elif e <= d <= t <= s:
    print(e * 1000 + d * 100 + t * 10 + s)
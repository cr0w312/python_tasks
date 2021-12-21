d = int(input())
month = int(input())
year = int(input())
if month >= 3:
    m = month - 2
elif month < 3:
    m = 10 + month
c = year // 100
if month > 3:
    y = year % 100
elif month <= 3:
    y = year % 100 - 1
weekday = (d + ((13 * m - 1) // 5) + y +
           (y // 4 + c // 4 - 2 * c + 777)) % 7
print(weekday)
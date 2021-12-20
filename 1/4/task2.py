pas1 = input()
pas2 = input()
if len(pas1) < 8:
    print("Короткий!")
elif pas1 != pas2:
    print("Различаются.")
else:
    print("OK")
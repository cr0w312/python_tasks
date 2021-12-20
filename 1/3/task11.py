num1 = input()
num2 = input()
znak = input()
if znak == "/" and float(num2) == 0:
    print("888888")
elif znak == "+":
    print(float(num1) + float(num2))
elif znak == "-":
    print(float(num1) - float(num2))
elif znak == "*":
    print(float(num1) * float(num2))
elif znak == "/":
    print(float(num1) / float(num2))
else:
    print("888888")
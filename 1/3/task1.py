g1 = input()
g2 = input()
if (g1 == "Тула" and g2 != "Пенза" and g2 != "Тула") or \
        (g1 != "Тула" and g1 != "Пенза" and g2 == "Пенза"):
    print("ДА")
else:
    print("НЕТ")

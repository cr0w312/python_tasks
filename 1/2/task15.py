a = "Перечитай первую инструкцию"
print("Ответь на следующие вопросы, назвав номер ответа из представленных")
print("Сколько часов в день ты проводишь в Интернете?")
print("1-Что такое Интернет? 2-Меньше часа 3-Около двух-трех часов 4-Больше")
q = input()
if q == "1" or q == "2" or q == "3" or q == "4":
    print("Что ты в основном делаешь в Интернете?")
    print("1-Что за Интернет? 2-Залипаю в новостной ленте \
3-Получаю полезную информацию? 4-Другое")
    w = input()
    if w == "1" or w == "2" or w == "3" or w == "4":
        print("Кто-любо когда-либо уличал тебя в интернет-зависимости?")
        print("1-Да кто этот ваш интернет? 2-Да, было дело 3-Нет \
        4-Я сам так считаю")
        e = input()
        if e == "1" or e == "2" or e == "3" or e == "4":
            print("Тест завершен.")
        else:
            print(a)
    else:
        print(a)
else:
    print(a)
if q == "1" and w == "1" and e == "1":
    print("Интернет это всемирная компьютерная сеть.. Короче спроси у Алисы")
elif (q == "1" and (w == "1" or w == "2" or w == "3" or w == "4") and
        (e == "2" or e == "3" or e == "4")):
    print("Ты прозрел в середине теста? XD")
elif (q == "2" or q == "3" or q == "4") and \
        (w == "1" or w == "2" or w == "3" or w == "4") and e == "1":
    print("У тебя случилась амнезия? Почему ты забыл, что такое Интернет?")
elif (q == "2" or q == "3" or q == "4") and w == "1" and \
        (e == "2" or e == "3" or e == "4"):
    print("Ты уж определись, знаешь ты про Интернет или нет..")
elif q == "2" and w == "3" and e == "3":
    print("Молодец! Будешь продолжать в том же духе и" + 
          " интернет-зависимость тебе не грозит")
elif (q == "2" and w == "3" and (e == "2" or e == "4")) or \
        (q == "2" and (w == "2" or w == "4") and e == "3") or \
        ((q == "3" or q == "4") and w == "3" and e == "3"):
    print("Неплохо! Но лучше немного начать себя ограничивать")
elif (q == "2" and (w == "2" or w == "4") and (e == "2" or e == "4")) or \
        ((q == "3" or q == "4") and w == "3" and (e == "2" or e == "4")) or \
        ((q == "3" or q == "4") and (w == "2" or w == "4") and e == "3"):
    print("Дело движется к зависимости. Плоховато, но пока не критично.")
elif (q == "3" or q == "4") and (w == "2" or w == "4") and \
        (e == "2" or e == "4"):
    print("Плохо дело;-; Видимо, придется ограничивать себя в интернете")
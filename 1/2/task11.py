print("Как прошел Ваш день?(ответ впишите строчными буквами)")
a = input()
hz = "Простите, я не совсем вас понимаю. Мой создатель \
еще слишком неопытен, чтобы обучить меня отвечать на такие \
сложные фразы..."
if ("не" in a) or ("?" in a):
    print(hz)
elif ("хорош" in a) or ("прекрасн" in a) or ("чудес" in a):
    print("Великолепно! У меня тоже)")
elif ("плох" in a) or ("ужас" in a) or ("отврат" in a):
    print("Не переживайте, все обязательно наладится")
else:
    print(hz)
klad_x = int(input())
klad_y = int(input())
player_x = 0
player_y = 0
player_dir = "север"
steps = 0
stop = 0
hodov = 0
direction = "север"
while stop != 1:
    command = input()
    steps = steps + 1
    points = 0
    if command not in "вперёд налево направо разворот стоп":
        print('не верная комманда')
    if command == 'вперёд':
        points = int(input())
    # передвигаем игрока
    if command == "вперёд":
        if player_dir == "север":
            player_y = player_y + points
        elif player_dir == "юг":
            player_y = player_y - points
        elif player_dir == "восток":
            player_x = player_x + points
        elif player_dir == "запад":
            player_x = player_x - points
    # если нужно развернуть, поворачиваем игрока
    if (command == "разворот" and player_dir == "север") or\
            (command == "налево" and player_dir == "запад") or\
            (command == "направо" and player_dir == "восток"):
        player_dir = "юг"
    elif (command == "разворот" and player_dir == "юг") or\
            (command == "налево" and player_dir == "восток") or\
            (command == "направо" and player_dir == "запад"):
        player_dir = "север"
    elif (command == "разворот" and player_dir == "запад") or\
            (command == "налево" and player_dir == "юг") or\
            (command == "направо" and player_dir == "север"):
        player_dir = "восток"
    elif (command == "разворот" and player_dir == "восток") or\
            (command == "налево" and player_dir == "север") or\
            (command == "направо" and player_dir == "юг"):
        player_dir = "запад"
    if klad_x == player_x and klad_y == player_y and command == "вперёд":
        hodov = steps
        direction = player_dir
    if command == "стоп" or hodov != 0:
        stop = 1
print(hodov)
print(direction)
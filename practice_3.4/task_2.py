count_player = int(input("Кол-во участников: "))
count_player_in_team = int(input("Кол-во человек в команде: "))

if count_player % count_player_in_team == 0:
    count_team = count_player // count_player_in_team
    commands = []
    last_player_num = 1
    for _ in range(count_team):
        commands.append(list(range(last_player_num, last_player_num + count_player_in_team)))
        last_player_num += count_player_in_team
    print(f"Общий список команд: {commands}")
else:
    print(f"{count_player} участников невозможно поделить на команды по {count_player_in_team} человек!")
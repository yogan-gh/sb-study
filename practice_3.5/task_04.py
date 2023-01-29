guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]
while True:
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
    command = input("Гость пришёл или ушёл? ")
    if command == "Пора спать":
        print("Вечеринка закончилась, все легли спать.")
        break
    elif command == "пришёл" or command == "ушёл":
        guest = input("Имя гостя: ")
        if command == "пришёл":
            if len(guests) == 6:
                print(f"Прости, {guest}, но мест нет.")
            else:
                guests.append(guest)
                print(f"Привет, {guest}!")
        elif command == "ушёл":
            if guests.count(guest):
                guests.remove(guest)
                print(f"Пока, {guest}!")
            else:
                print(f"Гостя с таким именем нет на вечеринке.")
    else:
        print("Команда не распознана.")

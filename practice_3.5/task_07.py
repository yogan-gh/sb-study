count_skates = int(input("Кол-во коньков: "))
list_skates = []

for i_num in range(1, count_skates + 1):
    skate_size = int(input(f"Размер {i_num}-й пары: "))
    list_skates.append(skate_size)

count_people = int(input("Кол-во людей: "))
list_people = []

for i_num in range(1, count_people + 1):
    people_size = int(input(f"Размер ноги {i_num}-го человека: "))
    list_people.append(people_size)

list_skates.sort()
list_people.sort()

max_count = 0

for people_size in list_people:
    skates_down = 0
    for skates_size in list_skates:
        if people_size <= skates_size:
            max_count += 1
            skates_down = skates_size
            break
    if skates_down:
        list_skates.remove(skates_down)

print(f"Наибольшее кол-во людей, которые могут взять ролики: {max_count}")

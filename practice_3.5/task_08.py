count_people = int(input("Кол-во человек: "))
num = int(input("Какое число в считалке? "))
print(f"Значит выбывает каждый {num}-й человек\n")
peoples = list(range(1, count_people + 1))
start_num = 0
while len(peoples) != 1:
    print(f"Текущий круг людей: {peoples}")
    print(f"Начало счёта с номера {peoples[start_num]}")
    exit_num = (num % len(peoples) + start_num) - 1
    if exit_num == -1:
        exit_num = len(peoples) - 1
    print(f"Выбывает человек под номером {peoples[exit_num]}\n")
    peoples.pop(exit_num)
    start_num = exit_num % len(peoples)
print(f"Остался человек под номером {peoples[0]}")
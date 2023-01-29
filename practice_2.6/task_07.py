def input_weight(message):
    while True:
        weight = int(input(message))
        if weight > 200:
            print("Вес контейнера не должен превышать 200! Повторите ввод.")
        else:
            return weight


pack_count = int(input("Количество контейнеров: "))
pack_list = []
for _ in range(pack_count):
    pack_weight = input_weight("Введите вес контейнера: ")
    pack_list.append(pack_weight)

pack_new_weight = input_weight("Введите вес нового контейнера: ")
for index in range(len(pack_list)):
    if pack_new_weight > pack_list[index]:
        print(f"Номер, который получит новый контейнер: {index + 1}")
        break

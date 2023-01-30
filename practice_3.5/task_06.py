list_one = []
list_two = []

for i in range(1, 4):
    num = int(input(f"Введите {i}-е число для первого списка: "))
    list_one.append(num)
for i in range(1, 8):
    num = int(input(f"Введите {i}-е число для второго списка: "))
    list_two.append(num)

print(f"Первый список: {list_one}")
print(f"Второй список: {list_two}")

list_one.extend(list_two)

list_uniq = []
for i_num in list_one:
    if not list_uniq.count(i_num):
        list_uniq.append(i_num)

print(f"Новый первый список с уникальными элементами: {list_uniq}")

list_num = [1, 4, -3, 0, 10]
print(f"Изначальный список: {list_num}")
unsorted = True
while unsorted:
    unsorted = False
    for index in range(len(list_num) - 1):
        if list_num[index] > list_num[index + 1]:
            unsorted = True
            list_num[index], list_num[index + 1] = list_num[index + 1], list_num[index]
print(f"Отсортированный список: {list_num}")

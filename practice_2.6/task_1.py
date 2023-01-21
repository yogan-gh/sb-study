count_num = int(input("Введите число: "))
list_num = []
for num in range(1, count_num + 1):
    if num % 2 != 0:
        list_num.append(num)

print("Список из нечётных чисел от одного до N:", list_num)
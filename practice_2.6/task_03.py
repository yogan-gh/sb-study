count = int(input("Количество клеток: "))
list_no_eff = []
for index in range(1, count + 1):
    print(f"Эффективность {index} клетки:", end=" ")
    eff = int(input())
    if eff < index:
        list_no_eff.append(eff)
print(f"Неподходящие значения: {list_no_eff}")

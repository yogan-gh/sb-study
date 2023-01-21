list_name = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
list_new_name = []
for index, name in enumerate(list_name):
    if index % 2 == 0:
        list_new_name.append(name)
print(f"Первый день: {list_new_name}")

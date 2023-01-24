list_elements = [1, 2, 3, 4, 5]
print(f"Изначальный список: {list_elements}")
list_new_elements = list_elements[1:] + list_elements[:1]
print(list_new_elements)

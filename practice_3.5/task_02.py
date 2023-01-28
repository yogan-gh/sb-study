class_one = list(range(160, 178, 2))
class_two = list(range(162, 183, 3))
print(class_one)
print(class_two)
class_main = []
class_main.extend(class_one)
class_main.extend(class_two)
class_main.sort()
print(f"Отсортированный список учеников: {class_main}")
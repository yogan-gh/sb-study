goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
new_fruit_name = input("Новый фрукт: ")
new_fruit_price = int(input("Цена: "))
goods.append([new_fruit_name, new_fruit_price])
print(f"Новый ассортимент: {goods}")
goods_up = []
for good in goods:
    good[1] += good[1] * 0.08
print(f"Новый ассортимент с налогом: {goods}")
shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
name_find = input('Название детали: ')
count = 0
total_price = 0
for name in shop:
    if name[0] == name_find:
        count += 1
        total_price += name[1]
print(f"Кол-во деталей — {count}")
print(f"Общая стоимость — {total_price}")

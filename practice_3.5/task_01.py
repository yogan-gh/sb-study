main = [1, 5, 3]
sub_one = [1, 5, 1, 5]
sub_two = [1, 3, 1, 5, 3, 3]

main.extend(sub_one)
print(f"Количество цифр 5: {main.count(5)}")
while main.count(5):
    main.remove(5)

main.extend(sub_two)
print(f"Количество цифр 3: {main.count(3)}")

print(main)
word = input("Введите слово: ")
letter_uni_list = []
for letter in word:
    if letter.isalpha() and letter not in letter_uni_list:
        letter_uni_list.append(letter)
print(f"Количество уникальных букв: {len(letter_uni_list)}")

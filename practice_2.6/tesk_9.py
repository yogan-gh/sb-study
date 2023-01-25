word = input("Введите слово: ")
word_list = list(word)
count_check = len(word) // 2
flag_pal = True
for index in range(1, count_check + 1):
    a = word_list[:1]
    b = word_list[-1:]
    if word_list[:1] != word_list[-1:]:
        flag_pal = False
        break
if flag_pal:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")

count_bits = int(input("Введите количество пакетов: "))
count_error_bits = 0
digital_msg = []

for i_bit in range(count_bits):
    print(f"Пакет номер {i_bit + 1}")
    bits = []
    for i in range(1, 5):
        bit = int(input(f"{i} бит: "))
        bits.append(bit)
    if bits.count(-1) > 1:
        count_error_bits += 1
        print("Много ошибок в пакете")
    else:
        digital_msg.extend(bits)
print(f"Полученное сообщение: {digital_msg}")
print(f"Кол-во ошибок в сообщении: {digital_msg.count(-1)}")
print(f"Кол-во потерянных пакетов: {count_error_bits}")

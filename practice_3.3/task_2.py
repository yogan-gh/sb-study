def count_ss(msg):
    return msg.count('!') + msg.count('?')


msg_first = input('Первое сообщение: ')
msg_second = input('Второе сообщение: ')

if count_ss(msg_first) > count_ss(msg_second):
    print(msg_first, msg_second)
elif count_ss(msg_first) < count_ss(msg_second):
    print(msg_second, msg_first)
else:
    print('Ой')

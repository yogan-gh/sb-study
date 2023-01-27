films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]

films_top = []

input_command = ''
while input_command != 'выход':
    print(f'\nВаш текущий топ фильмов: {films_top}')
    film = input('Название фильма: ')
    print('Команды: добавить, вставить, удалить, выход')
    input_command = input('Введите команду: ')
    if input_command == 'добавить':
        if not films.count(film):
            print('Такого фильма у нас нет')
        elif films_top.count(film):
            print('Фильм уже есть в избранном')
        else:
            films_top.append(film)
    elif input_command == 'вставить':
        if not films.count(film):
            print('Такого фильма у нас нет')
        else:
            position = int(input(f"В какое место вставить фильм? (от 0 до {len(films_top)})"))
            films_top.insert(position, film)
    elif input_command == 'удалить':
        if films_top.count(film):
            films_top.remove(film)
        else:
            print("В вашем списке нет такого фильма")
    elif input_command == 'выход':
        break
    else:
        print('Команда не найдена')

films = ["Крепкий орешек", "Назад в будущее",
         "Таксист", "Леон",
         "Богемская рапсодия",
         "Город грехов", "Мементо",
         "Отступники", "Деревня"]

count_film = int(input("Сколько фильмов хотите добавить? "))
film_like = []
for _ in range(count_film):
    film_name = input("Введите название фильма: ")
    if film_name not in films:
        print(f"Ошибка: фильма {film_name} у нас нет :(")
    else:
        film_like.append(film_name)
print(f"Ваш список любимых фильмов: {film_like}")
count_video_card = int(input("Количество видеокарт: "))
list_video_card = []
list_new_video_card = []
top_video_card = 0

for i in range(1, count_video_card + 1):
    print(f"{i} Видеокарта:", end=" ")
    video_card = int(input())
    list_video_card.append(video_card)
    if top_video_card < video_card:
        top_video_card = video_card
print(f"Старый список видеокарт: {list_video_card}")

for i in range(count_video_card):
    if list_video_card[i] != top_video_card:
        list_new_video_card.append(list_video_card[i])
print(f"Новый список видеокарт: {list_new_video_card}")
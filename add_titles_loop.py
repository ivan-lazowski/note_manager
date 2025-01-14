# titles = []
#
# while True:
#     user_input = input("Введите заголовок:")
#     if user_input == '':
#         break
#     if user_input == 'стоп':
#         break
#     elif user_input in titles:
#         print("Такой заголовок уже введен")
#     else:
#         titles.append(user_input)
# print(titles)


def main():
    notes = []  # Список для хранения заголовков заметок

    while True:
        title = input("Введите заголовок (или оставьте пустым для завершения): ")

        if not title:  # Если заголовок пустой, завершаем ввод
            break
        if title == 'стоп':
            break

        notes.append(title)  # Добавляем заголовок в список

    # Выводим список заголовков
    if notes:
        print("\nЗаголовки заметок:")
        for note in notes:
            print(f"- {note}")
    else:
        print("Заголовки не были введены.")


if __name__ == "__main__":
    main()
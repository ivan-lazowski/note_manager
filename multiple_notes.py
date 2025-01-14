def create_note():
    """Функция для создания новой заметки."""
    name = input("Введите имя заметки: ")
    title = input("Введите заголовок заметки: ")
    description = input("Введите описание заметки: ")
    status = input("Введите статус заметки: ")
    creation_date = input("Введите дату создания заметки (в формате ГГГГ-ММ-ДД): ")
    deadline = input("Введите дедлайн заметки (в формате ГГГГ-ММ-ДД): ")

    # Создаем словарь с данными заметки
    note = {
        "Имя": name,
        "Заголовок": title,
        "Описание": description,
        "Статус": status,
        "Дата создания": creation_date,
        "Дедлайн": deadline
    }

    return note


def display_notes(notes):
    """Функция для отображения всех заметок."""
    if not notes:
        print("Заметок пока нет.")
    else:
        for i, note in enumerate(notes, 1):
            print(f"Заметка #{i}:")
            for key, value in note.items():
                print(f"  {key}: {value}")
            print("-" * 30)


def main():
    """Основная функция программы."""
    notes = []  # Список для хранения заметок

    while True:
        command = input("Введите команду (добавить/стоп): ").strip().lower()

        if command == "добавить":
            note = create_note()
            notes.append(note)
            print("Заметка успешно добавлена!")
        elif command == "стоп":
            print("Завершение работы с заметками.")
            break
        else:
            print("Неизвестная команда. Попробуйте снова.")

        # Отображаем все заметки после каждой команды
        display_notes(notes)


if __name__ == "__main__":
    main()
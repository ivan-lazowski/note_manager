# Исходный список заметок
notes = [
    {"Имя": "Алексей", "Заголовок": "Список покупок", "Описание": "Купить продукты на неделю"},
    {"Имя": "Мария", "Заголовок": "Учеба", "Описание": "Подготовиться к экзамену"}
]


# Функция для отображения текущих заметок
def display_notes(notes):
    print("Текущие заметки:")
    for i, note in enumerate(notes, start=1):
        print(f"{i}. Имя: {note['Имя']}")
        print(f"   Заголовок: {note['Заголовок']}")
        print(f"   Описание: {note['Описание']}")
    print()


# Функция для удаления заметки по критерию
def delete_note(notes, criterion):
    # Создаем копию списка, чтобы не изменять оригинал во время итерации
    updated_notes = [note for note in notes if note['Имя'] != criterion and note['Заголовок'] != criterion]

    # Проверяем, изменился ли список
    if len(updated_notes) < len(notes):
        print(f"Успешно удалено. Остались следующие заметки:")
        display_notes(updated_notes)
        return updated_notes
    else:
        print(f"Заметок с таким именем пользователя или заголовком не найдено.")
        return notes


# Отображаем текущие заметки
display_notes(notes)

# Пользователь вводит критерий для удаления
criterion = input("Введите имя пользователя или заголовок для удаления заметки: ")

# Удаляем заметку и обновляем список
notes = delete_note(notes, criterion)
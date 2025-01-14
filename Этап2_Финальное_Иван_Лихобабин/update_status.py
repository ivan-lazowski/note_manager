def display_status(current_status):
    print(f'Текущий статус заметки: "{current_status}"')


def display_options():
    print('Выберите новый статус заметки:')
    print('1. выполнено')
    print('2. в процессе')
    print('3. отложено')


def get_user_choice():
    while True:
        try:
            choice = int(input('Ваш выбор: '))
            if 1 <= choice <= 3:
                return choice
            else:
                print('Пожалуйста, введите число от 1 до 3.')
        except ValueError:
            print('Пожалуйста, введите корректное число.')


def update_status(choice):
    statuses = {1: 'выполнено', 2: 'в процессе', 3: 'отложено'}
    return statuses[choice]


def main():
    # Изначальный статус заметки
    current_status = 'в процессе'

    # Отображаем текущий статус
    display_status(current_status)

    # Предлагаем варианты изменения статуса
    display_options()

    # Получаем выбор пользователя
    choice = get_user_choice()

    # Обновляем статус
    new_status = update_status(choice)

    # Выводим результат
    print(f'Статус заметки успешно обновлён на: "{new_status}"')


if __name__ == '__main__':
    main()

def showMenu():
    print('\nГлавное меню:\n'
          '\n1. Открыть TXT-файл\n'
          '2. Открыть CSV-файл\n'
          '3. Сохранить TXT-файл\n'
          '4. Сохранить CSV-файл(ANSI)\n'
          '5. Показать все контакты\n'
          '6. Поиск контакта\n'
          '7. Добавить конаткт\n'
          '8. Изменить контакт\n'
          '9. Удалить контакт\n'
          '0. Выход')


def inputInt(text: str):
    while True:
        try:
            number = int(input(text))
            return number
        except:
            print('Ошибка! Введите целое число!')


def inputStr(text: str):
    while True:
        try:
            string = input(text)
            return string
        except:
            print('Ошибка! Введите целое число!')


def showContacts(phone_book: list, textError: str):
    print()
    if not phone_book == []:
        for index, contact in enumerate(phone_book):
            print(index, *contact)
    else:
        print(textError)

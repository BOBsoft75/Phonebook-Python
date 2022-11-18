import model
import view


def start():
    while True:
        view.showMenu()
        choice = view.inputInt('Выберите пункт меню: ')
        match (choice):
            case 1:
                try:
                    openFile()
                    print('\nКнига загружена!')
                except:
                    print('Ошибка работы с файлом')
            case 2:
                try:
                    openFileCsv()
                    print('\nКнига загружена!')
                except:
                    print('Ошибка работы с файлом')
            case 3:
                try:
                    saveFile()
                    print('\nКнига сохранена!')
                except:
                    print('Ошибка работы с файлом')
            case 4:
                try:
                    saveFileCsv()
                    print('\nКнига сохранена!')
                except:
                    print('Ошибка работы с файлом')
            
            case 5:
                showAll()
            case 6:
                findContact()
            case 7:
                addContact()
            case 8:
                changeContact()
            case 9:
                deleteContact()
            case _:
                return False


def openFile():
    with open(model.getPath(), 'r', encoding='UTF-8') as data:
        phonebook = data.readlines()
        new_phonebook = []
        for contact in phonebook:
            new_contact = contact.replace('\n', '').split(';')
            new_phonebook.append(new_contact)
        model.setPhoneBook(new_phonebook)


def openFileCsv():
    with open(model.getPathCsv(), 'r', encoding='ANSI') as data:
        phonebook = data.readlines()
        new_phonebook = []
        for contact in phonebook:
            new_contact = contact.replace('\n', '').split(';')
            new_phonebook.append(new_contact)
        model.setPhoneBook(new_phonebook)


def saveFile():
    with open(model.getPath(), 'w', encoding='UTF-8') as data:
        new_phone_book = []
        for contact in model.getPhoneBook():
            new_phone_book.append(';'.join(contact))
        new_phone_book.sort()
        data.write('\n'.join(new_phone_book))


def saveFileCsv():
    with open(model.getPathCsv(), 'w', encoding='ANSI') as data: # для удобства просмотра результата в Excel кодировка сразу поменяна на ANSI
        new_phone_book = []
        for contact in model.getPhoneBook():
            new_phone_book.append(';'.join(contact))
        new_phone_book.sort()
        data.write('\n'.join(new_phone_book))


def showAll():
    phone_book = model.getPhoneBook()
    view.showContacts(phone_book, 'Телефонная книга пуста')


def findContact():
    phone_book = model.getPhoneBook()
    search = view.inputStr('Введите искомый элемент: ')
    search_book = []
    for contact in phone_book:
        for item in contact:
            if search in item:
                search_book.append(contact)
    view.showContacts(search_book, 'Контакт не найден')


def addContact():
    phone_book = model.getPhoneBook()
    contact = []
    contact.append(view.inputStr('Введите имя контакта: '))
    contact.append(view.inputStr('Введите телефон контакта: '))
    contact.append(view.inputStr('Введите комментарий для контакта: '))
    phone_book.append(contact)
    print('\nКонтакт добавлен')


def changeContact():
    phone_book = model.getPhoneBook()
    view.showContacts(phone_book, 'Телефонная книга пуста')
    choice = view.inputInt('Введите номер элемента для изменения: ')
    print(*phone_book.pop(choice))
    addContact()


def deleteContact():
    phone_book = model.getPhoneBook()
    view.showContacts(phone_book, 'Телефонная книга пуста')
    choice = view.inputInt('Введите номер элемента для удаления: ')
    phone_book.pop(choice)

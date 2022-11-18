path = 'Data/Phone.txt'
pathCsv = 'Data/Phone.csv'
phone_book = []
pathHtml = 'Data/index.html'


def getPath() -> str:
    global path
    return path


def getPathCsv() -> str:
    global pathCsv
    return pathCsv


def setPath(new_path: str):
    global path
    path = new_path


def getPhoneBook() -> list:
    global phone_book
    return phone_book


def setPhoneBook(new_phone_book: list):
    global phone_book
    phone_book = new_phone_book

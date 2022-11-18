
class PhoneBook:

    phone_book = []


    def getPhoneBook() -> list:
        global phone_book
        return phone_book

    def setPhoneBook(new_phone_book: list):
        global phone_book
        phone_book = new_phone_book

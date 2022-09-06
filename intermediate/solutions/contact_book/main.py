from typing import List


LIST_WIDTH = 60


class Contact:

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return self.name

    @classmethod
    def from_prompt(cls):
        name = input('Enter full name: ')
        email = input('Enter email address: ')
        phone = input('Enter phone number: ')
        if not name and not phone and not email:
            raise ValueError('trying to add contact with no data')
        return cls(name=name, email=email, phone=phone)

    def display_list(self):
        print('+', '-' * (LIST_WIDTH - 2), '+', sep='')
        print('|  🙍 ', self.name.upper().ljust(LIST_WIDTH - 9), '  |', sep='')
        print('|  📧 ', self.email.ljust(LIST_WIDTH - 9), '  |', sep='')
        print('|  📞 ', self.phone.ljust(LIST_WIDTH - 9), '  |', sep='')
        print('+', '-' * (LIST_WIDTH - 2), '+', sep='')


class ContactBook:
    def __init__(self) -> None:
        self.contacts: List[Contact] = []

    def add_contact(self):
        self.contacts.append(Contact.from_prompt())

    def view_list(self):
        for contact in self.contacts:
            contact.display_list()

    def view_table(self):
        raise NotImplementedError

    def show_menu(self):
        raise NotImplementedError


if __name__ == '__main__':
    book = ContactBook()
    book.add_contact()
    book.add_contact()
    book.view_list()
    # user.display_list()
    # book.show_menu()

class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def validate_phone_number(phone_number):
        if len(phone_number) == 10:
            return True
        return False

class ContactList:
    all_contacts = []

    @staticmethod
    def add_contact(name, phone_number):
         if Contact.validate_phone_number(phone_number):
             new = Contact(name, phone_number)
             ContactList.all_contacts.append(new)
         else:
             raise ValueError('В номере некорректное число цифр, трубется 10')


print(ContactList.all_contacts)

ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)

ContactList.add_contact("БИН", "045555")

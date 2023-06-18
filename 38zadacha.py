import os

class Contact:
    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

class Phonebook:
    def __init__(self, file_name):
        self.contacts = []
        self.file_name = file_name
        self.load_from_file()

    def add_contact(self, name, surname, phone_number):
        self.contacts.append(Contact(name, surname, phone_number))

    def search_by_surname(self, surname):
        matching_contacts = []
        for contact in self.contacts:
            if contact.surname.lower() == surname.lower(): #Введенная строка переводится в нижний регистр
                matching_contacts.append(contact)
        return matching_contacts

    def edit_contact(self, index, name, surname, phone_number):
        self.contacts[index - 1] = Contact(name, surname, phone_number)

    def delete_contact(self, index):
        del self.contacts[index - 1]

    def view_all_contacts(self):
        for contact in self.contacts:
            print(f"{contact.name} {contact.surname} - {contact.phone_number}")

    def export_to_file(self):
        with open(self.file_name, 'w', encoding = "utf-8") as f:
            for contact in self.contacts:
                f.write(f"{contact.name},{contact.surname},{contact.phone_number}\n")

    def load_from_file(self):
        if os.path.isfile(self.file_name):
            with open(self.file_name, 'r', encoding = "utf-8") as f:
                for line in f:
                    name, surname, phone_number = line.strip().split(',')
                    self.contacts.append(Contact(name, surname, phone_number))

def main():
    phonebook = Phonebook("phonebook.txt")
    while True:
        print("Доступные действия:\n1 - Добавить контакт \n2 - Поиск контактов (по фамилии) \n3 - Редактировать контакт \n4 - Удалить контакт \n5 - Посмотреть все записанные контакты \n6 - Выйти из программы")
        choice = input("Укажите номер действия: ")

        if choice == "1":
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            phone_number = input("Введите номер телефона: ")
            phonebook.add_contact(name, surname, phone_number)
            phonebook.export_to_file()

        elif choice == "2":
            surname = input("Введите фамилию: ")
            matching_contacts = phonebook.search_by_surname(surname)
            if matching_contacts:
                for contact in matching_contacts:
                    print(f"{contact.name} {contact.surname} - {contact.phone_number}")
            else:
                print("Извините, указанного контакта не найдено. Попробуйте ввести другую фамилию.")

        elif choice == "3":
            index = int(input("Введите № контакта который вы хотите отредактировать: "))
            name = input("Введите новое имя (если требуется): ")
            surname = input("Введите новую фамилию (если требуется): ")
            phone_number = input("Введите новый номер телефона (если требуется): ")
            phonebook.edit_contact(index, name, surname, phone_number)
            phonebook.export_to_file()

        elif choice == "4":
            index = int(input("Введите № контакта который вы хотите удалить: "))
            phonebook.delete_contact(index)
            phonebook.export_to_file()

        elif choice == "5":
            phonebook.view_all_contacts()

        elif choice == "6":
            break
        else:
            print("ПУНКТОВ ВСЕГО ШЕСТЬ! ШЕСТЬ, КАРЛ! Выбери пожалуйста от 1 до 6!")

if __name__ == "__main__":
    main() #Запускает бесконечный цикл, предлагая выбирать действие. Будет предлагать до того момента пока пользователь не введет цифру 6.
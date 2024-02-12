"""
Задача №55 Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
- Программа должна выводить данные
- Программа должна сохранять данные в текстовом файле
- Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
- Использование функций. Ваша программа не должна быть линейной
"""

# 1. Создание файла:
# - открываем файл на дозапись # a
# 2. Добавление контакта:
# - запросить у пользователя новый контакта
# - открыть файл на дозапись # a
# - добавить новый контакт
# 3. Вывод данных на экран:
# - открыть файл на чтение # r
# - считать файл
# - вывести на экран
# 4. Поиск контакта:
# - выбор варианта поиска
# - запросить данные для поиска
# - открыть файл на чтение
# - считываем данные файла, сохранить их в переменную
# - осуществляем поиск контакта
# - выводим на экран найденный контакта
# 5. Создание UI:
# - вывести меню на экран
# - запросить у пользавателя вариант действия
# - запустить соответствующую функцию
# - осуществить возможность выхода из программы


def input_surname():
    return input("Input surname of the contact: ")


def input_name():
    return input("Input name of the contact: ")


def input_patronymic():
    return input("Input patronymic of the contact: ")


def input_phone():
    return input("Input phone of the contact: ")


def input_address():
    return input("Input address(city) of the contact: ")


def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f"{surname} {name} {patronymic}: {phone}\n{address}\n\n"


def add_contact():
    contact = create_contact()
    with open("phonebook.txt", "a", encoding="utf-8") as file:
        file.write(contact)


def print_contact():
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        print(file.read())


def search_contact():
    print(
        "Search options: \n",
        "1. by surname\n",
        "2. by name\n",
        "3. by patronymic\n",
        "4. by phone\n",
        "5. by address\n",
    )
    var = input("Select search option: ")
    while var not in ("1", "2", "3", "4", "5"):
        print("Incorrect input")
        var = input("Select search option: ")

    idx_var = int(var) - 1
    

    search = input("Input data for search: ")
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contacts_str = file.read()

    contacts_list = contacts_str.rstrip().split("\n\n")

    for contact_str in contacts_list:
        contact_lst = contact_str.replace(":", "").split()
        # print(f"{idx_var=} {search=} {contact_lst[idx_var]=}")
        if search in contact_lst[idx_var]:
            print(contact_str)
        print()


def interface():
    with open("phonebook.txt", "a", encoding="utf-8"):
        pass

    var = 0
    while var != '4':
        print(
            "Options: \n",
            "1. Add contact\n",
            "2. Print contacts\n",
            "3. Search contact\n",
            "4. Exit",
        )
        print()
        var = input("Select an option: ")
        while var not in ("1", "2", "3", "4"):
            print("Incorrect input")
            var = input("Select an option: ")
        print()

        match var:
            case "1":
                add_contact()
            case "2":
                print_contact()
            case "3":
                search_contact()
            case "4":
                print("Good bye!")

        return


if __name__ == "__main__":
    interface()

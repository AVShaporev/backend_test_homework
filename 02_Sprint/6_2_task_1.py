class Contact:
    def __init__(self, name, phone, birthday):
        self.name = name
        self.phone = phone
        self.birthday = birthday

    def show_contact(self):
        print(self)

mike = Contact('Михаил Булгаков', '2-03-27', '15.05.1891')
vlad = Contact('Владимир Маяковский', '73-88', '19.07.1893')

mike.show_contact()
vlad.show_contact()
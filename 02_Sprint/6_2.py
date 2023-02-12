class Contact:
    def __init__(self, name, phone, birthday):
        self.name = name
        self.phone = phone
        self.birthday = birthday

        print(f'Создан новый контакт {name}')

    def show(self):
        print(f'Имя: {self.name}, телефон: {self.phone}, день рождения: {self.birthday}')

    def __str__(self):
        return 'Контакт: ' + self.name

# Создание объекта
ivan = Contact('Иван', '+559845651651', '02.12.1985')

ivan.show()

print(ivan)
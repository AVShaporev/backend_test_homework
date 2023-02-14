from datetime import datetime


class Record:
    def __init__(self, amount=0, comment='', date=datetime.strftime(datetime.now(), '%d.%m.%Y')):
        self.amount = amount
        self.comment = comment
        self.date = datetime.strptime(date, '%d.%m.%Y')
        self.USD_RATE = 0.013581
        self.EURO_RATE = 0.012711

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        self.rem = self.limit - sum(i.amount for i in self.records if datetime.strftime(i.date, '%d.%m.%Y')
                                    == datetime.strftime(datetime.now(), '%d.%m.%Y'))
        if currency == 'rub':
            self.rem = self.rem * 1
        elif currency == 'usd':
            self.rem = self.rem * self.USD_RATE
        else:
            self.rem = self.rem * self.EURO_RATE
        if self.rem > 0:
            return (f'На сегодня осталось {self.rem} {currency}')
        elif self.rem == 0:
            return (f'Денег нет, держись')
        else:
            return (f'Денег нет, держись: твой долг - {abs(self.rem)} {currency}')


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        self.rem = self.limit - sum(i.amount for i in self.records if datetime.strftime(i.date, '%d.%m.%Y')
                                    == datetime.strftime(datetime.now(), '%d.%m.%Y'))
        if self.rem > 0:
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.rem} кКал')
        else:
            return ('Хватит есть!')



# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)

# дата в параметрах не указана,
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе"))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))

print(cash_calculator.get_today_cash_remained("rub"))
# должно напечататься
# На сегодня осталось 555 руб


r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.")
r5 = Record(amount=84, comment="Йогурт.")
r6 = Record(amount=1140, comment="Баночка чипсов.")

ccal_calculator = CaloriesCalculator(2000)

ccal_calculator.add_record(r4)
print(ccal_calculator.get_calories_remained())

ccal_calculator.add_record(r5)
print(ccal_calculator.get_calories_remained())

ccal_calculator.add_record(r6)
print(ccal_calculator.get_calories_remained())



class Date:
    def __init__(self, day, month, year):
        self.date = day, month, year

    @property
    def day(self):
        return self.date[0]

    @property
    def month(self):
        return self.date[1]

    @property
    def year(self):
        return self.date[3]

    @classmethod
    def unpack(cls, date):
        aux = [int(i) for i in date.split('-')]
        day, month, year = aux
        if not Date.validate(day, month, year):
            print("no such date:")
        return cls(day, month, year)

    @staticmethod
    def is_leap(year):
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

    @staticmethod
    def validate(day, month, year):
        if month < 1 or month > 12:
            return False
        days_in_month = {1: 31, 2: 29 if Date.is_leap(year) else 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30,
                         10: 31, 11: 30, 12: 31}
        return True if 1 <= day <= days_in_month[month] else False


print(Date.unpack('29-02-2020').date)
print(Date.unpack('29-02-2021').date)  # такой даты не существует, будет выведено сообщение об ошибке

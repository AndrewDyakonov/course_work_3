class Operation:
    """"""
    def __init__(self, date, description, to, currency, summa, from_=None):
        self.date = date
        self.description = description
        self.to = to
        self.currency = currency
        self.summa = summa
        self.from_ = from_

    def beautiful_data(self):
        """Вывод даты в формате ДД.ММ.ГГГГ"""
        clear_data = self.date[:10]
        result = clear_data[8:] + '.' + clear_data[5:7] + '.' + clear_data[:4]
        return result

    def beautiful_card_number(self):
        """Возвращает номер карты в требуемом формате"""
        text = str(self.from_)
        if sum(c.isdigit() for c in text) == 16:
            result = self.from_[:-12] + ' **' + '** **** ' + self.from_[-4:]
            return result

    def __repr__(self):
        return f'{self.date}, {self.description}, {self.to}, {self.currency}' \
               f'{self.summa}, {self.from_}'

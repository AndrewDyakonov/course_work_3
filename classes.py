class Operation:
    """"""
    def __init__(self, date, description, to, currency, summa, from_=None):
        self.date = date
        self.description = description
        self.to = to
        self.currency = currency
        self.summa = summa
        self.from_ = from_


# < дата перевода > < описание перевода >
# < откуда > -> < куда >
# < сумма перевода > < валюта >

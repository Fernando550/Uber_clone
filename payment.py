class Payment:
    def __init__(self, date):
        self.id = id
        self.date = date


class Card(Payment):
    def __init__(self, date, cardNumber, CVV):
        super().__init__(date)
        self.cardNumber = cardNumber
        self.integer = CVV

class Paypal(Payment):
    def __init__(self, date, email):
        super().__init__(date)
        self.email = email

class Cash(Payment):
    def __init__(self, date):
        super().__init__(date)
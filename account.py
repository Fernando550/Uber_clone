import random

# super class
class Account:
    def __init__(self, name, document, email, pasword):
        self.id = id
        self.name = name
        self.document = document
        self.email = email
        self.pasword = pasword

    def check_inf():
        pass

# Child classes
class Driver(Account):
    def __init__(self, name, document, email, pasword):
        super().__init__(name, document, email, pasword)

class User(Account):
    def __init__(self, name, document, email, pasword):
        super().__init__(name, document, email, pasword)
        self.position = self.define_position()

    def define_position(self):
        positionX = random.randint(-100, 100)
        positionY = random.randint(-100, 100)

        return (positionX, positionY)


       
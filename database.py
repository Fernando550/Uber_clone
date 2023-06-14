import account
from car import UberBan, UberBlack, UberPool, UberX
import random


users = [
    account.User(
    "Fernando",
    "1234",
    "fernando268a@gmail.com",
    "wawa"),
    account.User(
        "Tom",
        "2347",
        "tom@gmail.com",
        "mama"
    )
]

drivers = [
    account.Driver(
        "Kyel",
        "2468",
        "kyle@gmail.com",
        "car"
    ),
    account.Driver(
        "Michale",
        "2435",
        "michile@gmail.com",
        "car2"
    ),
    account.Driver(
        "Sara",
        "0694",
        "sara@gmail.com",
        "tax"
    ),
]

brands_x_black = [
    "Tsla",
    "Chevie",
    "Porche",
    "BWW"
]

brands_Ban_pool = [
    "Tsla",
    "Chevie",
    "Porche",
    "BWW"
]

driver = random.choice(drivers)
print(driver)
model = random.randint(2010, 2023)

uberX = UberX(driver.name, driver.document,random.choice(brands_x_black),model)

uberBlack = UberBlack(driver.name, driver.document,random.choice(brands_x_black),model)

uberBan = UberBan(driver.name, driver.document,random.choice(brands_Ban_pool),model)

uberPool = UberPool(driver.name, driver.document,random.choice(brands_Ban_pool),model)

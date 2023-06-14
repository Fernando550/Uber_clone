
from payment import Payment
from route import Route
from database import users,uberBan,uberPool,uberX,uberBlack
from map import map
import time


def loginUser(userName,pasword):
    for user in users:
        if user.name != userName:
            continue
        else:
            if user.pasword != pasword:
                print("your pasword is not correct!")
                quit()
            else:
                return user
    print("The user you tipe in doesn't exist!")
    quit() 

def make_bill(distance, objetUber):
    cost  = distance * 3
    time.sleep(2)
    print(f"the cost of the trip will be {cost}")
    print(f"the driver will be {objetUber.driver}")
    print("Confirm your trip: ")
    confirmation = input()
    confirmation.lower()
    if confirmation == "yes" or confirmation == "y":
        print("Than you for choosing Uber")
    else:
        print("have a nice day! good bye")
        quit()

def run():
    print("Hi wellcome to Uber please login to start a trip! =)")

    username = input("User Name: ")
    if username.isdigit():
        print("Tipe a real name next time!")
        quit()
    else:
        username = username.lower()
        username = username.capitalize()

    pasword = input("Enter password: ")
    
    user = loginUser(username,pasword) 

    print(f"-----Wellcome to Uber {user.name}-------")

    print(map)

    print(f"you courent position is :{user.position}")
    route = Route(user)
    distance = route.get_distance() # distance

    print("uberX = 1,uberBan = 2,uberPool = 3,uberBlack = 4")

    car_choose =  input("in wich uber do you want to go: ")

    if car_choose == "1":
        car_choose = uberX
    elif car_choose == "2":
        car_choose = uberBan
    elif car_choose == "3":
        car_choose = uberPool
    elif car_choose == "4":
        car_choose = uberBlack
    else:
        print("Pleace select a real option next time!")
        quit()
    
    make_bill(distance,car_choose)
    

if __name__== "__main__":
    run()



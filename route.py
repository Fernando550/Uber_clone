
class Route:
    HOME = (0,0)
    MALL = (-23, 45)
    SHOOLD = (90, 20)
    WORK = (-75, 35)

    def __init__(self, user):
        self.id = id
        self.start = user.position
        self.end = ()
        self.user = user
        self.get_destination()

    def get_destination(self):
        print(''' 
        HOME = H
        SHOOLD = S
        MALL = M
        WORK = W
        ''')
        destination = input("Where do you whant to go? chose by chosing a letter: ")
        destination = destination.upper()
        print(destination)
        if destination == "H":
            self.end = self.HOME
        elif destination == "S":
            self.end = self.SHOOLD
        elif destination == "M":
            self.end = self.MALL
        elif destination == "W":
            self.end = self.WORK

    def get_distance(self):
        distanceX = self.end[0] - self.start[0]
        distanceY = self.end[1] - self.start[1]

        if distanceX < 0:
            distanceX = distanceX * -1

        if distanceY < 0:
            distanceY = distanceY * -1
        
        return distanceX + distanceY
     




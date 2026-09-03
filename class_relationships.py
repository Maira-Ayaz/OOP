#COMPOSITION(has a / dependent )
class Room:
    def __init__(self, room_name):
        self.room_name = room_name

    def show_room(self):
        print("Room:", self.room_name)


class House:
    def __init__(self):
        self.room = Room("Bedroom")   # Room object created inside House

    def show_house(self):
        print("House contains:")
        self.room.show_room()


h1 = House()
#r1 = Room("dinning room")
#r1.show_room()
h1.show_house()
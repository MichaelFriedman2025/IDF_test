

class Building:

    def __init__(self,rooms:int = 10,beds_in_every_room:int = 8):
        self.rooms = rooms
        self.beds_in_every_room = beds_in_every_room
        self.buildings = {}

        self.add_building("Dorm A")
        self.add_building("Dorm B")


    def add_building(self,name_of_building):
        building = []
        for i in range(self.rooms):
            room = []
            for j in range(self.beds_in_every_room):
                room.append(None)
            building.append(room)
        self.buildings[name_of_building] = building


from operator import index
from models.buildings import Building


class ManagementBase:
    def __init__(self,buildings:Building,soldiers):
        self.buildings = buildings.buildings
        self.soldiers = soldiers

        self.assigning_soldiers_into_beds()

    def number_of_available_beds(self):
        counter_of_beds = 0
        for building in  self.buildings.values():
            for room in building:
                for bed in room:
                    if not bed:
                        counter_of_beds += 1
        return counter_of_beds

    def max_soldier_distance_from_the_base(self):
        num = self.number_of_available_beds()
        were_assigned = []
        all_distance_from_the_base = []
        for soldier in self.soldiers:
            num = int(soldier.distance_from_the_base)
            all_distance_from_the_base.append(num)

        while num != 0 and all_distance_from_the_base:
            max_distance_from_the_base = max(all_distance_from_the_base)
            for soldier in self.soldiers:
                num = int(soldier.distance_from_the_base)
                if num == max_distance_from_the_base:
                    if soldier.placement_status == "waiting":
                        were_assigned.append(soldier)
                        num -= 1
            num_index = all_distance_from_the_base.index(max_distance_from_the_base)
            all_distance_from_the_base.pop(num_index)
        return were_assigned


    def assigning_soldiers_into_beds(self):
        soldiers_for_deployment = self.max_soldier_distance_from_the_base()
        for building in  self.buildings.values():
            for room in building:
                for bed in range(len(room)):
                    if not soldiers_for_deployment:
                        break
                    else:
                        soldier = soldiers_for_deployment.pop()
                        soldier.placement_status = "inserted"
                        room[bed] = soldier


    def soldiers_waiting_to_be_deployed(self):
        soldiers_waiting = []
        for soldier in self.soldiers:
            if soldier.placement_status == "waiting" :
                soldiers_waiting.append(soldier)
        return soldiers_waiting


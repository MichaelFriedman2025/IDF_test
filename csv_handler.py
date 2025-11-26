from models.buildings import Building
from models.class_base import BaseCSV
from models.management_base import ManagementBase


def load_and_save_data_from_scv_and_return_data(temp_file):
    base_csv = BaseCSV(temp_file)
    base_csv.load_soldiers_into_the_base()
    buildings = Building()
    management_base = ManagementBase(buildings,base_csv.soldiers)
    return summary_of_the_data(management_base)

def summary_of_the_data(management_base):
    count_assigned = len(management_base.max_soldier_distance_from_the_base())
    count_waiting = len(management_base.soldiers_waiting_to_be_deployed())
    list_of_all_soldiers_with_info = get_soldiers_waiting_to_be_deployed(management_base) + get_assigning_soldiers_into_beds(management_base)
    return {"the number of soldiers assigned":f"{count_assigned}",
            "the number of soldiers waiting":f"{count_waiting}",
            "the details of all soldiers":f"{list_of_all_soldiers_with_info}"}

def get_soldiers_waiting_to_be_deployed(management_base):
    result = []
    soldier_list = management_base.soldiers_waiting_to_be_deployed()
    for soldier in soldier_list:
        result.append({"id_number":f"{soldier.id_number}","not assigned":"He is on the waiting list."})
    return result

def get_location_of_soldier_bed(management_base,id_number) -> tuple | None:
    result = None
    for name,building in management_base.buildings.items():
        for room in building:
            for bed in range(room):
                if room[bed].id_number == id_number:
                    result =  (name,bed)
    return result


def get_assigning_soldiers_into_beds(management_base):
    result = []
    soldier_list = management_base.max_soldier_distance_from_the_base()
    for soldier in soldier_list:
        res = get_location_of_soldier_bed(management_base,soldier.id_number)
        if res:
            result.append({"id_number": f"{soldier.id_number}", "assigned": f"He is on the building {res[0]} at room {res[1]}."})
    return result






def checking_if_id_soldier_its_correct(id_number:str) -> bool:
    if id_number.isdigit() and id_number.startswith("8"):
        return True
    return False



import csv
from io import StringIO

from Validations.checking_soldier import checking_if_id_soldier_its_correct
from models.soldier import Soldier


class BaseCSV:
    def __init__(self,file):
        self.file = file
        self.soldiers = []

    def load_soldiers_into_the_base(self):
        decoded = self.file.read().decode('utf-8')
        reader = csv.DictReader(StringIO(decoded))
        for row in reader:
            soldier = Soldier(row["מספר אישי"],row["שם פרטי"],row["שם משפחה"],row["מין"],row["עיר מגורים"],row["מרחק מהבסיס"])
            if checking_if_id_soldier_its_correct(soldier.id_number):
                self.soldiers.append(soldier)






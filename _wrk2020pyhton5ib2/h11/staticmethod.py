class Dates:
    def __init__(self, date):
        self.date = date
        
    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

a_date = Dates("15-12-2016")
date_from_db = "15/12/2016"
date_with_dash = Dates.toDashDate(date_from_db)

if a_date.getDate() == date_with_dash:
    print("Equal")
else:
    print("Unequal")

print("-----------------")
tekst1 = "15-12-2016"
tekst2 = "15/12/2016"

if tekst1 == tekst2:
    print("tekst1 en tekst2 zijn gelijk")
else:
    print("tekst1 en tekst2 zijn niet gelijk")

    
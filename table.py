class Table:
    # creating a table 
    def __init (self):
        self.occupant=[seat(),seat(),seat(),seat()]
list_tabels=[]
for i in range(6):
    list_tabels.append(Table)
print(list_tabels)
class OpenSpace:
    def init(self):
        self.tables = [Table(), Table(), Table(), Table(), Table(), Table()]
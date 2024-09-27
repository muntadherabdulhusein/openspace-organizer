import random
Colleagues=["Adheeba","Anastasiia", "Basma", "Dhrisya","Ihor","Izabela","Kelli","Kevin","Levin","Maarten","Majid","Minh Duc","Moustafa",
            "Muntadher","Nicolaas","Petra","Rasmita","Rik","Soha","Tom","Urson","Veena","Wouter","Yeliz","Yusra","Zelimkhan"]
print(Colleagues)
class Seat:
  #This is a seat

  def init(self):
    self.free = True
    self.occupant = ""

  def setoccupant(self,name):
    self.free = False
    self.occupant = name

  def removeoccupant(self):
    self.free = True
    self.occupant = ""

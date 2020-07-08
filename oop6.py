#07 - Private Variable
class Hero:#template
    #class variable
    jumlah = 0
    def __init__(self,inputName,inputHealth, inputPower, inputArmor):
        # instance variable
        self.name    = inputName
        self.health  = inputHealth
        self.power   = inputPower
        self.armor   = inputArmor
        # instance private variable
        self.__private = "private"
        # instance protected variable
        self._protected = "protected"
        # class variable
        Hero.jumlah+=1

lina = Hero("Liba",  100 ,10  ,4)
print(lina.__dict__)
# lina.__private = "testing1"
lina._protected = "testing2"
print(lina.__dict__)
# print(lina.__protected)
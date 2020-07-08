#05 - Latihan OOP sederhana
class Hero:#template
    #class variable
    jumlah = 0
    def __init__(self,inputName,inputHealth, inputPower, inputArmor):
        # instance variable
        self.name    = inputName
        self.health  = inputHealth
        self.power   = inputPower
        self.armor   = inputArmor
        Hero.jumlah+=1

    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.power)

    def diserang(self, lawan, powerLawan):
        print(self.name + ' diserang ' + lawan.name)
        self.health -= powerLawan/self.armor
        print('serangan terasa: ' + str(self.health))

Sniper = Hero("Sniper",  100 ,10  ,4)
Sven   = Hero("Sven"  ,  100 ,15  ,5) 

Sniper.serang(Sven)
print('\n')
Sven.serang(Sniper)
print('\n')
Sven.serang(Sniper)
print('\n')
Sven.serang(Sniper)
print('\n')
Sven.serang(Sniper)
print('\n')
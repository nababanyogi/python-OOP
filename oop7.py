#08 - Encapsulasi
class Hero:
    #class variable
    jumlah = 0
    def __init__(self,name,health, power, armor):
        # instance variable
        self.__name    = name
        self.__health  = health
        self.__power   = power
        self.__armor   = armor
        # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health
    
    # setter
    def diserang(self, serangPower):
        self.__health -= serangPower

sniper = Hero("Sniper",  100 ,10  ,4)
print(sniper.__dict__)
print(sniper.getName())
sniper.diserang(10)
print(sniper.getHealth())


 
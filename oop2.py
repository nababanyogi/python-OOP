#03 - Class dan Instance variables
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
        print("membuat Hero dengan nama "+inputName)

hero1 = Hero("Sniper",  100 ,10  ,4)
print(Hero.jumlah)
hero2 = Hero("Sven"  ,  100 ,15  ,1)  
print(Hero.jumlah)
hero3 = Hero("Mirana",  1000,100 ,0)
print(Hero.jumlah)

# print(hero1.__dict__)
# print(hero2.__dict__)
# print(hero3.__dict__)

# print(hero1)
# print(hero2)
# print(hero3)
# print(Hero.__dict__)

#04 - Methods
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
        # print("membuat Hero dengan nama "+inputName)

    # void function, method tanpa return    
    def siapa(self):
        print("namaku adalah "+ self.name)
    
    # method dengan argumen dan
    def healthUp(self, up):
        self.health+=up

    # method dengan return
    def getHealth(self):
        return self.health
    


hero1 = Hero("Sniper",  100 ,10  ,4)
hero2 = Hero("Sven"  ,  100 ,15  ,1)  
hero3 = Hero("Mirana",  1000,100 ,0)

# print(hero1.__dict__)
hero1.siapa()
hero1.healthUp(10)
print(hero1.getHealth())
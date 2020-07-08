#14 - Override Method
class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} dengan health {}".format(
            self.name, 
            self.health
            )
        )

class Hero_intelligent(Hero):
    def __init__(self,name):
        super().__init__(name,100)

    #override
    def showInfo(self):
        print("{} : \nTipe : Inteligent,\nHealth : {}".format(
            self.name,
            self.health
            )
        )


class Hero_strength(Hero):
    def __init__(self,name):
        super().__init__(name,200)
class Hero_agility(Hero):
    def __init__(self,name):
        super().__init__(name,150)

techies = Hero_intelligent('techies')
axe = Hero_strength('axe')
slark = Hero_agility('slark')

techies.showInfo()
axe.showInfo()
slark.showInfo()

# print(techies.__dict__)
# print(axe.__dict__)
# print(slark.__dict__)
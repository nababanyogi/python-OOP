#12 - Pendahuluan Inheritance
# class hero adalah 
class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

class Hero_intelligent(Hero):
    pass
class Hero_strength(Hero):
    pass
class Hero_agility(Hero):
    pass

lina = Hero('lina', 100)
techies = Hero_intelligent('techies', 50)
axe = Hero_strength('axe', 50)
slark = Hero_agility('slark', 50)

print(lina.name)
print(techies.name)
print(axe.name)
print(slark.name)

print(lina.__dict__)
print(techies.__dict__)
print(axe.__dict__)
print(slark.__dict__)
# print(help(lina))
# print(help(techies))

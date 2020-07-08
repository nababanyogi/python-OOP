#10 - Getter dan Setter
class Hero:
    def __init__(self, name, health, armor):
        self.__name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name : {}  \n\thealth : {}".format(self.__name,self.__health)

    # def getHealth(self):
    #     return self.__health

    #mengubah method menjadi seperti variable
    @property
    def info(self):
        return "name : {}  \nhealth : {}".format(self.__name,self.__health)
    @property
    def armor(self):
        pass
    @armor.getter
    def armor(self):
        return self.__armor
    @armor.setter
    def armor(self,input):
        self.__armor = input
    @armor.deleter
    def armor(self):
        self.__armor = None
        print('armor di delete')

sniper = Hero('sniper', 100, 10)
# print(sniper.getHealth())
print(sniper.__dict__)
print(sniper.info)
print(sniper.armor)
sniper.armor = 30
print(sniper.armor)
del sniper.armor
print(sniper.armor)
print(sniper.__dict__)


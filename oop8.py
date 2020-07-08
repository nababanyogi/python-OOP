#09 - Staticmethod dan Classmethod
class Hero:

    __jumlah=0

    def __init__(self,name):
        self.__name = name
        Hero.__jumlah +=1

    # hanya berlaku untuk object
    def getJumlah_A(self):
        return Hero.__jumlah
    # method ini tidak berlaku utk object tp class   
    def getJumlah_B():
        return Hero.__jumlah
    # method static (decorator) > berlaku ke class dan method
    @staticmethod
    def getJumlah_C():
        return Hero.__jumlah
    
    @classmethod
    def getJumlah_D(cls):
        return cls.__jumlah

sniper = Hero('sniper')
rikimaru = Hero('rikimaru')
drowranger = Hero('drowranger')
# print(Hero.__jumlah)
print(sniper.getJumlah_A())
print(Hero.getJumlah_B())
print(sniper.getJumlah_C())
print(Hero.getJumlah_C())
print(sniper.getJumlah_D())
print(Hero.getJumlah_D())
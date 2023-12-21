import mettt
class med:
    def __init__ (self,name_of_medi , colvo):
        self.name_of_medi = name_of_medi
        self.colvo=colvo
class medd(med):
    def __init__ (self , name_of_medi ,   proizvod , colvo ):
        super().__init__(name_of_medi , colvo)
        
        self.proizvod = proizvod
        

med1 = medd("Ибупрофен" , "Россия" , 5)
med2 = medd("Пропитал" , "США" , 5)
med3 = medd("P22" , "Германия" , 5)
med4 = medd("Звездочка" , "Вьетнам" , 5)





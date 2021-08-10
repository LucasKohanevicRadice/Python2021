# Tässä tehtävässä käydään pythonissa valmiina olevia vertailumetodeja.


class Raha:
    def __init__(self, eurot: int, sentit: int):

        self.__eurot = eurot
        sentit /= 100
        self.__sentit = sentit

        self.__rahamaara = float(self.__eurot + self.__sentit)

    def __str__(self):
        
        return f"{self.__rahamaara:.2f} eur" #   :.2f MÄÄRITTELEE DESIMAALIEN MÄÄRÄN NÄYTETTÄVÄKSI KAHTEEN DESIMAALIIN. KAHDEN DESIMAALIN TARKKUUDELLA SIIS.
    

        
    def __eq__(self, toinen) -> bool:
        return self.__rahamaara == toinen.__rahamaara
    
    def __lt__(self, toinen):
        return self.__rahamaara < toinen.__rahamaara
    
    def __gt__(self,toinen):
        return self.__rahamaara > toinen.__rahamaara
    
    def __ne__(self, toinen) -> bool:
        return self.__rahamaara != toinen.__rahamaara
    
    def __add__(self,toinen):
         self.__uusi_summattu = (self.__rahamaara + toinen.__rahamaara)
         return f"{self.__uusi_summattu:.2f} eur"

    def __sub__(self, toinen):
        if (self.__rahamaara - toinen.__rahamaara) >= 0:
            self.__uusi_erotettu = (self.__rahamaara - toinen.__rahamaara)
            return f"{self.__uusi_erotettu:.2f} eur"
            
        else:
            raise ValueError("Erotus ei saa päätyä negatiiviseen lukuun.")
        

        

# e1 = Raha(4, 10)
# e2 = Raha(2, 5)
# e3 = Raha(4, 10)

# print(e1)
# print(e2)
# print(e3)
# print(e1 == e2)
# print(e1 == e3)
# print(e1 < e2)
# print(e1 > e2)
# print(e1 != e2)

if __name__ == "__main__":
    e1 = Raha(1, 0)
    e2 = Raha(2, 0)
    print(e1-e2)

    # e3 = e1 + e2
    # # e4 = "{:.2f}".format((e1 - e2))   #   Tässä yks tapa
    # e4 = e1 - e2


    # print(e3)
    # print(f"{e4:.2f}")  #   Jos haluaa käyttää tätä muotoa, niin se pitää olla f-merkkijono muodossa.

    # e5 = e2-e1
    # print(e5)








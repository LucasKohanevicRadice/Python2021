# tee ratkaisusi tänne

class Opintosuoritukset:

    def __init__(self) -> None:

        self.__SuoritettukurssiJaArvosana = {}
        self.__opintopisteet = 0
        self.__kurssi_OP = {}
        self.__arvosanatYht = 0


    def lisaa_suoritus(self, kurssi: str, arvosana: int, opintopisteet: int):

        if arvosana not in range(1,6):
            raise ValueError("Anna arvosana välillä 1-5")
        
        elif kurssi in self.__SuoritettukurssiJaArvosana:
            if self.__SuoritettukurssiJaArvosana[kurssi] > arvosana:
                raise ValueError("Et voi laskea kurssiarvosanaa")
        
        else:
            self.__SuoritettukurssiJaArvosana[kurssi] = arvosana
            self.__arvosanatYht += arvosana
            self.__kurssi_OP[kurssi] = opintopisteet
            self.__opintopisteet += opintopisteet

        
    def hae_suoritus(self, kurssi: str):

        if kurssi in self.__kurssi_OP:

            return f"{kurssi} ({self.__kurssi_OP[kurssi]} op), arvosana {self.__SuoritettukurssiJaArvosana[kurssi]}"
            
        else: 
            return "Kurssisuoritusta ei löytynyt"
    

    def tilasto_taulukko(self):

        X = "X"

        self.__vitoset = f"5: {(sum(value == 5 for value in self.__SuoritettukurssiJaArvosana.values()))*X}"
        self.__neloset = f"4: {(sum(value == 4 for value in self.__SuoritettukurssiJaArvosana.values()))*X}"
        self.__kolmoset =f"3: {(sum(value == 3 for value in self.__SuoritettukurssiJaArvosana.values()))*X}"
        self.__kakkoset = f"2: {(sum(value == 2 for value in self.__SuoritettukurssiJaArvosana.values()))*X}"
        self.__ykkoset = f"1: {(sum(value == 1 for value in self.__SuoritettukurssiJaArvosana.values()))*X}"
            

    
    def tilastot(self):
        
        Opintosuoritukset.tilasto_taulukko(self)

        return f"""Suorituksia {len(self.__SuoritettukurssiJaArvosana)} kurssilta, yhteensä {self.__opintopisteet} opintopistettä
Keskiarvo: {(self.__arvosanatYht/len(self.__SuoritettukurssiJaArvosana)):.2f}
Arvosanajakauma:
{self.__vitoset}
{self.__neloset}
{self.__kolmoset}
{self.__kakkoset}
{self.__ykkoset}"""
    


# kalle = Opintosuoritukset()

# kalle.lisaa_suoritus("ohpe", 3)
# print(kalle.hae_suoritus("ohpe"))
# print(kalle.tilastot())




class InterActive():

    def __init__(self) -> None:

        self.__rekisteri = Opintosuoritukset()
        
    

    def suorita(self):

        komennot = [1,2,3,0]
        print("1 Lisää suoritus\n2 Hae suoritus\n3 Tilastot\n0 Lopetus")
        while True:

            try:

                komento = int(input("Komento: "))
                if komento == 1:
                    lisättävä_kurssi = input("Lisättävä kurssi: ")
                    lisättävä_arvosana = int(input("Lisättävä arvosana: "))
                    lisättävä_opintopiste = int(input("Lisää opintopisteet: "))
                    self.__rekisteri.lisaa_suoritus(lisättävä_kurssi, lisättävä_arvosana, lisättävä_opintopiste)
                    
        
                elif komento == 2:
                    haettava_suoritus = input("Haettava kurssi: ")
                    print(self.__rekisteri.hae_suoritus(haettava_suoritus))
            
                elif komento == 3:
                    print(self.__rekisteri.tilastot())
            
                elif komento == 0:
                    print("Heisulivei")
                    break
            
            except:
                print("Komentojen pitää olla 1,2,3 tai 0")
                


            # if komento not in komennot:
            #     raise ValueError("Komentojen pitää olla 1,2,3 tai 0")
        

            # if komento == 1:
            #     lisättävä_kurssi = input("Lisättävä kurssi: ")
            #     lisättävä_arvosana = int(input("Lisättävä arvosana: "))
            #     lisättävä_opintopiste = int(input("Lisää opintopisteet: "))
            #     print(self.__rekisteri.lisaa_suoritus(lisättävä_kurssi, lisättävä_arvosana, lisättävä_opintopiste))
        
            # elif komento == 2:
            #     haettava_suoritus = input("Haettava kurssi: ")
            #     print(self.__rekisteri.hae_suoritus(haettava_suoritus))
            
            # elif komento == 3:
            #     print(self.__rekisteri.tilastot())
            
            # elif komento == 0:
            #     print("Heisulivei")
            #     break
            


kallenKoulu = InterActive()

kallenKoulu.suorita()





        


       
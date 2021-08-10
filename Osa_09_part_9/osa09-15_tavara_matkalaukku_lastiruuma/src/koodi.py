# Tee ratkaisusi tähän:
# Tee ratkaisusi tähän:

class Tavara:
    
    def __init__(self, nimi: str, paino: int) -> None:

        self.__nimi = nimi
        self.__paino = paino

    @property
    def nimi(self):

        return self.__nimi

    @nimi.setter
    def nimi(self):
        self.__nimi = nimi
        
    @property
    def paino(self):

        return self.__paino
        
    @paino.setter
    def paino(self):
        self.__paino = paino

        pass









class Matkalaukku:

    def __init__(self, maksimipaino: int) -> None:

        self.__maksimipaino = maksimipaino
        self.__current_paino = 0
        self.__tavara_lkm = 0
        self.__tavarat = []
    
    def lisaa_tavara(self, tavara: Tavara):

        if tavara.paino > self.__maksimipaino: #    Eli ei voi kutsua suoraan piilotettua oliota luokan Tavara sisältä. Pitää kutsua metodin "paino" kautta (property)
            raise PermissionError("Tavaran paino ylittää sallitun painomäärän")

        elif (tavara.paino + self.__current_paino) > self.__maksimipaino:
            raise PermissionError("Tavaran paino ylittää sallitun painomäärän")

        else:
            self.__current_paino += tavara.paino
            self.__tavara_lkm += 1
            self.__tavarat.append(f"{tavara.nimi} ({tavara.paino} kg)")
    
    @property
    def paino(self):
        return int(self.__current_paino)
    
    @paino.setter
    def paino(self):
        self.__current_paino = self.__current_paino

    

    def tulosta_tavarat(self):

        for tavara in self.__tavarat:
            print(tavara)
    

    def painon_palautus(self):
        return(f"Yhteispaino: {self.__current_paino} kg")
    

    def raskain_tavara(self):
        raskain = None

        for tavara in self.__tavarat:

            osat = tavara.split(" ")
            paino = int(osat[-2])

            if raskain == None:
                raskain = tavara

            elif paino > int(raskain[-4]):
                raskain = tavara

            
        raskain_osat = raskain.split(",")
        raskain_nimi = raskain_osat[0]
        raskain_paino = raskain_osat[1]
        raskain_paino = raskain_paino.strip()
        

        return f"Raskain tavara: {raskain_nimi} ({raskain_paino})"
        
 
    def __str__(self) -> str:

        if self.__tavara_lkm == 1:
            return (f"{self.__tavara_lkm} tavara ({self.__current_paino} kg)")
        else:
            return (f"{self.__tavara_lkm} tavaraa ({self.__current_paino} kg)")

        pass









class Lastiruuma:

    def __init__(self, maksimipaino: int) -> None:

        self.__maksimipaino = maksimipaino
        self.__ruumanPaino = 0
        self.__matkalaukkujenLKM = 0
        self.__matkalaukut = []

    
    def lisaa_matkalaukku(self, matkalaukku:Matkalaukku):
        

        if (self.__ruumanPaino + matkalaukku.paino) > self.__maksimipaino:
            raise PermissionError("Painoraja ylittyy, vähennä kuormaa")

        else:
            self.__ruumanPaino += matkalaukku.paino # Muokkaa matkalaukku luokkaan paino propertyt ja setterit jos tää (self.__currentpaino) ei toimi
            self.__matkalaukut.append(matkalaukku)
            self.__matkalaukkujenLKM += 1
    

    def tulosta_tavarat(self):

        for matkalaukku in self.__matkalaukut:
            matkalaukku.tulosta_tavarat()


    
    def __str__(self) -> str:

        if self.__matkalaukkujenLKM == 1:
            return f"{self.__matkalaukkujenLKM} laukku, tilaa {self.__maksimipaino - self.__ruumanPaino} kg"
        
        elif self.__matkalaukkujenLKM == 0 or self.__matkalaukkujenLKM > 1:
            return f"{self.__matkalaukkujenLKM} laukkua, tilaa {self.__maksimipaino-self.__ruumanPaino} kg"
        
        pass






# kirja = Tavara("aapinen", 2)
# puhelin = Tavara("Nokia 3310", 1)
# tiiliskivi = Tavara("Brick", 4)
# leipa = Tavara("BRÖDDIS", 1)
# juoma = Tavara("ISO KOKIS", 2)
# print(kirja.paino)
# print(kirja.nimi)


# matkalaukku = Matkalaukku(10)

# matkalaukku.lisaa_tavara(kirja)
# print(matkalaukku)

# matkalaukku.lisaa_tavara(puhelin)
# print(matkalaukku)

# matkalaukku.lisaa_tavara(tiiliskivi)
# print(matkalaukku)

# matkalaukku.lisaa_tavara(juoma)
# print(matkalaukku)

# matkalaukku.lisaa_tavara(leipa)
# matkalaukku.tulosta_tavarat()

# print(matkalaukku.raskain_tavara())

# ruuma = Lastiruuma(1000)

# ruuma.lisaa_matkalaukku(matkalaukku)
# print(ruuma)

# matkalaukku_v2 = Matkalaukku(10)

# matkalaukku_v2.lisaa_tavara(kirja)
# matkalaukku_v2.lisaa_tavara(puhelin)
# matkalaukku_v2.lisaa_tavara(tiiliskivi)
# matkalaukku_v2.lisaa_tavara(leipa)

# print(matkalaukku_v2)

# ruuma.lisaa_matkalaukku(matkalaukku_v2)
# print(ruuma)

# ruuma.tulosta_tavarat()

kirja = Tavara("Aapiskukko", 2)
puhelin = Tavara("Nokia 3210", 1)

print("Kirjan nimi:", kirja.nimi())
print("Kirjan paino:", kirja.paino())

print("Kirja:", kirja)
print("Puhelin:", puhelin)
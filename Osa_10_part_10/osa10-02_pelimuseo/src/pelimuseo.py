# TEE RATKAISUSI TÄHÄN:
class Tietokonepeli:
    def __init__(self, nimi: str, julkaisija: str, vuosi: int):
        self.nimi = nimi
        self.julkaisija = julkaisija
        self.vuosi = vuosi

class Pelivarasto:
    def __init__(self):
        self.__pelit = []

    def lisaa_peli(self, peli: Tietokonepeli):
        self.__pelit.append(peli)

    def anna_pelit(self):
        return self.__pelit


class Pelimuseo(Pelivarasto):

    def __init__(self):
        super().__init__()
        self.__vanhat = []

    
    # def lisaa_peli(self, peli: Tietokonepeli):
    #     self.__pelit.append(peli)
    
    
    def anna_pelit(self):

        for peli in super().anna_pelit():
            if peli.vuosi < 1990:
                self.__vanhat.append(peli)
        return self.__vanhat


if __name__ == "__main__":
    gta_v = Tietokonepeli("GTA V", "ROCKSTAR", 2014)
    gow = Tietokonepeli("God Of War", "Santa monica studios", 2018)
    pac_man = Tietokonepeli("Pac Man", "tetris", 1800)

    museo = Pelimuseo()

    museo.lisaa_peli(gow)
    museo.lisaa_peli(pac_man)



    for peli in museo.anna_pelit():
        print(peli.nimi)


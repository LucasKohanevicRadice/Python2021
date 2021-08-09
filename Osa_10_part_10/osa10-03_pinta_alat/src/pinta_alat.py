# TEE RATKAISUSI TÄHÄN:
class Suorakulmio:
    def __init__(self, leveys: int, korkeus: int):
        self.leveys = leveys
        self.korkeus = korkeus

    def __str__(self):
        return f"suorakulmio {self.leveys}x{self.korkeus}"

    def pinta_ala(self):
        return self.leveys * self.korkeus


class Nelio(Suorakulmio):

    def __init__(self, sivu: int):

        korkeus = sivu
        leveys = sivu

        super().__init__(leveys, korkeus)
        
    def __str__(self):
        return f"neliö {self.leveys}x{self.leveys}"
    
    def pinta_ala(self):
        return (self.leveys * self.leveys)
    




class SuorakulmainenKolmio(Suorakulmio):

    def __init__(self, leveys: int, korkeus: int):

        super().__init__(leveys, korkeus)
    

    def __str__(self):
        return f"Suorakulmainen kolmio {self.korkeus}x{self.leveys}"
    
    def pinta_ala(self):
        return (self.leveys*self.korkeus)/2


if __name__ == "__main__":
    nelio = Nelio(4)

    print(nelio)

    print("pinta-ala:", nelio.pinta_ala())



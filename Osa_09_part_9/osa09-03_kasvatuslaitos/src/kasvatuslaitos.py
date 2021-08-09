
# TEE RATKAISUSI TÄHÄN:
# Huom! Älä muuta luokkaa Henkilo!

class Henkilo:
    def __init__(self, nimi: str, ika: int, pituus: int, paino: int):
        self.nimi = nimi
        self.ika = ika
        self.pituus = pituus
        self.paino = paino

class Kasvatuslaitos:
    def __init__(self):
        self.punnitusten_lkm = 0

    def syota(self, henkilo: Henkilo):

        henkilo.paino += 1

        


    
    def punnitukset(self):

        return self.punnitusten_lkm

    def punnitse(self, henkilo: Henkilo):
        # palautetaan parametrina annetun henkilön paino
        self.punnitusten_lkm += 1

        return henkilo.paino


if __name__ == "__main__":
    sepi = Henkilo("seppo", 3, 37, 86)   
    k1 = Kasvatuslaitos()
    k1.syota(sepi)



    print(f"{sepi.nimi} painaa saatana {k1.punnitse(sepi)} vaikka on vaan saatana {sepi.ika}-vuotias" )   #   MUISTA TÄÄ SAATANAN ONGELMA. 
#   OIKEA MUOTO ON Kasvatuslaitos().punnitse, eikä Kasvatuslaitos.punnitse



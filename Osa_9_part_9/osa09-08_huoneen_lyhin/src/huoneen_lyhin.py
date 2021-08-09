# TEE RATKAISUSI TÄHÄN:
class Henkilo:
    def __init__(self, nimi: str, pituus: int):
        self.nimi = nimi
        self.pituus = pituus

    def __str__(self):
        return self.nimi

class Huone:

    def __init__(self) -> None:

        self.hlo_lista = []
        self.skäbä = None

        pass

    def lisaa(self,henkilo: Henkilo):

        self.hlo_lista.append(henkilo)
    
    def on_tyhja(self):

        if len(self.hlo_lista) == 0:
            return True

        elif len(self.hlo_lista) > 0:
            return False

        # elif len(self.hlo_lista) < 0:
        #     raise ValueError("Huoneessa ei voi olla negatiivista määrää ihmisiä dumdum")

    def tulosta_tiedot(self):

        yhteispituus = 0

        for hlö in self.hlo_lista:
            yhteispituus += hlö.pituus

        print(f"Huoneessa {len(self.hlo_lista)} henkilöä, yhteispituus {yhteispituus} cm")

        for henkilö in self.hlo_lista:
            print(f"{henkilö.nimi} ({henkilö.pituus} cm)")
    
    def lyhin(self):

        if len(self.hlo_lista) == 0:
            return None

        self.skäbä = self.hlo_lista[0]

        for henkilö in self.hlo_lista:
            if henkilö.pituus < self.skäbä.pituus:
                self.skäbä = henkilö


        return self.skäbä
    
    def poista_lyhin(self):

        if len(self.hlo_lista) == 0:
            return None

        self.skäbbis = self.lyhin()

        self.hlo_lista.remove(self.lyhin())

        return self.skäbbis



    def loytyy(self):

        for indeksi, arvo in enumerate(self.hlo_lista):
            if arvo == self.skäbä:
                print("löytyy!!")
        




if __name__ == "__main__":
    huone = Huone()

    huone.lisaa(Henkilo("Lea", 183))
    huone.lisaa(Henkilo("Kenya", 182))
    huone.lisaa(Henkilo("Nina", 172))
    huone.lisaa(Henkilo("Auli", 186))
    huone.tulosta_tiedot()

    print()

    poistettu = huone.poista_lyhin()
    print(f"Otettiin huoneesta {poistettu.nimi}")

    print()

    huone.tulosta_tiedot()

    huone.loytyy()


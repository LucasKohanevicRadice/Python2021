# Tee ratkaisusi tähän:
class Muistilista:

    def __init__(self, otsikko: str, merkinnat: list) -> None:

        self.otsikko = otsikko
        self.merkinnat = merkinnat
        
        pass

if __name__ == "__main__":

    pannaanit = Muistilista("pannaneita", ["kappaleita", "no vittu", 4])

    print(pannaanit.merkinnat)


class Asiakas:

    def __init__(self, tunniste: str, saldo: float, alennusprosentti: int) -> None:

        self.tunniste = tunniste
        self.saldo = saldo
        self.alennusprosentti = alennusprosentti
        pass


class Kaapeli:

    def __init__(self, malli: str, pituus: float, maksiminopeus: int, kaksisuuntainen: bool) -> None:

        self.malli = malli
        self.pituus = pituus
        self.maksiminopeus = maksiminopeus
        self.kaksisuuntainen = kaksisuuntainen

        pass
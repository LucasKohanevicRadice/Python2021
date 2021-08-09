class Palloilija:
    def __init__(self, nimi: str, pelinumero: int, maalit: int, syotot: int, minuutit: int):
        self.nimi = nimi
        self.pelinumero = pelinumero
        self.maalit = maalit
        self.syotot = syotot
        self.minuutit = minuutit

    def __str__(self):
        return (f'Palloilija(nimi={self.nimi}, pelinumero={self.pelinumero}, '
            f'maalit={self.maalit}, syotot={self.syotot}, minuutit={self.minuutit})')

# TEE RATKAISUSI TÄHÄN:


def eniten_maaleja(palloilijat: list):

    jogadores = []

    def vahimmasta_enimpaan_maaleja(palloilija: Palloilija):

        return palloilija.maalit
    
    for pelaaja in palloilijat:
        jogadores.append(pelaaja)

    jogadores.sort(key = vahimmasta_enimpaan_maaleja, reverse= True)

    return str(jogadores[0].nimi)



def eniten_pisteita(palloilijat: list):

    champion = palloilijat[0]

    for pelaaja in palloilijat:
        if (pelaaja.maalit + pelaaja.syotot) > (champion.maalit + champion.syotot):
            champion = pelaaja

        else:
            champion = champion
    
    palautus = (champion.nimi, champion.pelinumero)
    
    return palautus


def vahiten_minuutteja(palloilijat: list):

    jogadores = []

    def maarittelyehto_minuutit(palloilija: Palloilija):

        return palloilija.minuutit
    
    for pelaaja in palloilijat:
        jogadores.append(pelaaja)
    
    jogadores.sort(key = maarittelyehto_minuutit)

    return jogadores[0]












if __name__ == "__main__":
    pelaaja1 = Palloilija("Kelju Kojootti", 13, 5, 12, 46)
    pelaaja2 = Palloilija("Maantiekiitäjä", 7, 2, 26, 55)
    pelaaja3 = Palloilija("Uka Naakka", 9, 1, 32, 26)
    pelaaja4 = Palloilija("Pelle Peloton", 12, 1, 11, 41)
    pelaaja5 = Palloilija("Hessu Hopo", 4, 3, 9, 12)
    joukkue = [pelaaja1, pelaaja2, pelaaja3, pelaaja4, pelaaja5]

    print(eniten_maaleja(joukkue))
    print(eniten_pisteita(joukkue))
    print(vahiten_minuutteja(joukkue))
        



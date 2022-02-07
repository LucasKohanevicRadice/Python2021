# Tässä tehtävässä käytetään listakoosteita. Tehtävänä oli kirjoittaa funktio, joka palauttaa listakoosteita hyödyntäen kaikki suoritusten parhaat arvosanat.
# Suoritukset annetaan funktioon listana ja funktio poimii listasta parhaat arvosanat.
# Funktion maksimipituus sai olla kokonaisuudessaan kaksi riviä, sisältäen myös funktion määrittelevän rivin.


class Koesuoritus:
    def __init__(self, nimi: str, arvosana1: int, arvosana2: int, arvosana3: int):
        self.nimi = nimi
        self.arvosana1 = arvosana1
        self.arvosana2 = arvosana2
        self.arvosana3 = arvosana3

    def __str__(self):
        return (f'Nimi:{self.nimi}, arvosana1: {self.arvosana1}' +
            f', arvosana2: {self.arvosana2}, arvosana3: {self.arvosana3}')


def parhaat_tulokset(suoritukset: list):

    return [max(luku.arvosana1, luku.arvosana2, luku.arvosana3) for luku in suoritukset]
    
if __name__ == "__main__":
    suoritus1 = Koesuoritus("Pekka",5,3,4)
    suoritus2 = Koesuoritus("Pirjo",3,4,1)
    suoritus3 = Koesuoritus("Paavo",2,1,3)
    suoritukset = [suoritus1, suoritus2, suoritus3]
    print(parhaat_tulokset(suoritukset))




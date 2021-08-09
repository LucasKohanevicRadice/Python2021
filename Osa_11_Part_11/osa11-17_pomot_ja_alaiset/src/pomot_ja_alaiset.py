# TEE RATKAISUSI TÄHÄN:
class Tyontekija:
    def __init__(self, nimi: str):
        self.nimi = nimi
        self.alaiset = []

    def lisaa_alainen(self, tyontekija: 'Tyontekija'):
        self.alaiset.append(tyontekija)


def laske_alaiset(duunari: Tyontekija):

    maara = len(duunari.alaiset)

    if duunari.nimi is not None:
        maara += laske_alaiset(duunari)
    




t1 = Tyontekija("Sasu")
t2 = Tyontekija("Erkki")
t3 = Tyontekija("Matti")
t4 = Tyontekija("Emilia")
t5 = Tyontekija("Antti")
t6 = Tyontekija("Kjell")
t1.lisaa_alainen(t4)
t1.lisaa_alainen(t6)
t4.lisaa_alainen(t2)
t4.lisaa_alainen(t3)
t4.lisaa_alainen(t5)
print(laske_alaiset(t1))
print(laske_alaiset(t4))
print(laske_alaiset(t5))
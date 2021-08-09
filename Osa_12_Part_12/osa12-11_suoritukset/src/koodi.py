class Suoritus:
    def __init__(self, opiskelijan_nimi: str, kurssi: str, arvosana: int):
        self.opiskelijan_nimi = opiskelijan_nimi
        self.kurssi = kurssi
        self.arvosana = arvosana

    def __str__(self):
        return f"{self.opiskelijan_nimi}, arvosana kurssilta {self.kurssi} {self.arvosana}"

# Tee ratkaisusi tähän:



def suorittajien_nimet(suoritukset: list):

    nimet = map(lambda suoritus : suoritus.opiskelijan_nimi, suoritukset)

    # nimilista = list(nimet)

    return [nimi for nimi in nimet]





def kurssien_nimet(suoritukset: list):

    kurssit = map(lambda suoritus: suoritus.kurssi, suoritukset)

    kurssit = list(kurssit)

    for indeksi,kurssi in enumerate(kurssit):
        if kurssit.count(kurssi) > 1:
            kurssit.pop(indeksi)

    return sorted([kurssi for kurssi in kurssit])


if __name__ == "__main__":
    s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
    s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
    s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 2)
    lista = [s1,s2,s3]

    print(suorittajien_nimet(lista))
    print(kurssien_nimet(lista))


#   Tehtävänanto hämmentää. Omasta mielestä tehtävää ei voi tehdä tehtävänannossa haetulla tavalla. map funktio ei toimi, jos parametriksi antaa listan.
# if __name__ == "__main__":
#     s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
#     s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
#     s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 2)

#     lista = [s1,s2,s3]

#     suorittajat = map(suorittajien_nimet,lista)

#     for suorittaja in suorittajat:
#         print(suorittaja)

#     suorituksessa = map(kurssien_nimet, lista)

#     for kurssi in suorituksessa:
#         print(kurssi)

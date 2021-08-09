# tee ratkaisu tänne


def lisaa_opiskelija(opiskelijat: dict, nimi: str):

    opiskelijat[nimi] = {}


def tulosta(opiskelijat: dict, nimi: str):

    if nimi not in opiskelijat:
        print(f"ei löytynyt ketään nimellä {nimi}")
        return

    opiskelijan_suoritukset = opiskelijat[nimi]

    print(f"{nimi}:")
    if len(opiskelijan_suoritukset) == 0:
        print(" ei suorituksia")

    else:
        print(f" suorituksia {len(opiskelijan_suoritukset):} kurssilta:")
        summa = 0
        for kurssi, suoritus in opiskelijan_suoritukset.items():
            arvosana = suoritus[1]
            print(f"  {kurssi} {arvosana}")
            summa += arvosana

        print(f" keskiarvo {summa/len(opiskelijan_suoritukset):.1f}")

def lisaa_suoritus(opiskelijat: dict, nimi: str, suoritus: tuple):

    opiskelijan_suoritukset = opiskelijat[nimi]
    kurssi = suoritus[0]
    arvosana = suoritus[1]

    if arvosana == 0:
        return

    if kurssi in opiskelijan_suoritukset:
        if opiskelijat[kurssi][1] > arvosana:
            return

    opiskelijan_suoritukset[kurssi] = suoritus

    def kooste(opiskelijat: dict):

        print(f"opiskelijoita {len(opiskelijat)}")

        eniten_lkm = 0
        paras_ka = 0

        for nimi, suoritukset in opiskelijat.items():
            if len(suoritukset) > eniten_lkm:
                eniten = nimi
                eniten_lkm = len(opiskelijat[eniten])

        summa = 0
        for kurssi, suoritus in suoritukset.items():
            summa += suoritus[1]

        if len(suoritukset) == 0:
            ka = 0

        else:
            ka = summa/len(suoritukset)

        if ka > paras_ka:
            paras_ka = ka
            paras = nimi

        print(f"eniten suorituksia {eniten} {eniten}")
        print(f"paras keskiarvo {paras_ka:.1f} {paras}")
    


# if __name__ == "__main__":

    # opiskelijat = {}
    # lisaa_opiskelija(opiskelijat, "pekka")
    # lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 5))
    # lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 1))
    # tulosta(opiskelijat, "pekka")


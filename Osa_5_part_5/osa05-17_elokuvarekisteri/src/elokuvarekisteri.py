# tee ratkaisu tänne

def lisaa_elokuva(rekisteri: list, nimi: str, ohjaaja: str, vuosi: int, pituus: int):

    elokuva = {"nimi": nimi,
              "ohjaaja": ohjaaja,
              "vuosi": vuosi,
              "pituus": pituus}

    rekisteri.append(elokuva)


if __name__ == "__main__":
    rik_rek= []
    lisaa_elokuva(rik_rek, "saapasjalkakissa", "pertti", 1420, 2)
    lisaa_elokuva(rik_rek, "shrek", "louis", 69, 23 )
    lisaa_elokuva(rik_rek,"paska leffa", "taboul", 1, -1)
    print(rik_rek)
# tee ratkaisu tänne

def suurin():

    with open("luvut.txt") as tiedosto:

        suurin_luku = 0

        for rivi in tiedosto:
            if int(rivi) > suurin_luku:
                suurin_luku = int(rivi)
    
    return suurin_luku


if __name__ == "__main__":
    print(suurin())
 
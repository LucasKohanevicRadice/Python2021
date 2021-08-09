# tee ratkaisu tänne

def lue_hedelmat():

    hedelmat = {}


    with open("hedelmat.csv") as tiedosto:

        for rivi in tiedosto:
            
            osat = rivi.split(";")
            
            hedelma = osat[0]
            hinta = float(osat[1])

            hedelmat[hedelma] = hinta
    
    return hedelmat


if __name__ == "__main__":
    print(lue_hedelmat())

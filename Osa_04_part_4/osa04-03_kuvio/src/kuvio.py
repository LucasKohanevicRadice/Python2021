# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäen
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti


def viiva(luku, merkkijono):

    if merkkijono == "":
        merkkijono = "*"
        print(luku*merkkijono)

    else:
        print(luku*merkkijono[0])



def kuvio(tri_num: int, tri_mark: str, sqr_num: int, sqr_mark: str):

    for i in range(0, tri_num+1):
        viiva(i,tri_mark)
    
    for i in range(0,sqr_num):
        viiva(tri_num,sqr_mark)






if __name__ == "__main__":
    kuvio(5, "x", 3, "*")

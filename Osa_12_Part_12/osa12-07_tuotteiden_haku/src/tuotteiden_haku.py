# TEE RATKAISUSI TÄHÄN:

def hae(tuotteet: list, kriteeri: callable):

    todennetut_osat = []

    for tuote in tuotteet:
        if kriteeri(tuote) == True:
            todennetut_osat.append(tuote)
    
    return todennetut_osat




def hinta_alle_4_euroa(tuote : tuple):

    return tuote[1] < 4


    # alle_4ssä_eurossa = []
    # for tuote in tuotteet:
    #     if tuote[1] < 4.00:
    #         return tuote


if __name__ == "__main__":
    tuotteet = [("banaani", 5.95, 12), ("omena", 3.95, 3), ("appelsiini", 4.50, 2), ("vesimeloni", 4.95, 22), ("Kaali", 0.99, 1)]

    for tuote in hae(tuotteet, hinta_alle_4_euroa):
        print(tuote)
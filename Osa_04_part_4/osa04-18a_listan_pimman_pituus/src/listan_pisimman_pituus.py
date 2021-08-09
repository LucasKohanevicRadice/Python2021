# tee ratkaisu tänne



def pisimman_pituus(lista : list):

    lista.sort(key=len)
    
    pisin_sana = lista[-1]

    return len(pisin_sana)




if __name__ == "__main__":
    pisimman_pituus(["peevee", "auts", "seepee"])


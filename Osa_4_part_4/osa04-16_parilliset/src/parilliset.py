# tee ratkaisu tänne


def parilliset(lista : list):

    lista2 = []

    for luku in lista:
        if luku % 2 == 0:
            lista2.append(luku)
    return lista2

if __name__ == "__main__":

    lista = [1, 2, 3, 4, 5]
    uusi_lista = parilliset(lista)
    print("alkuperäinen", lista)
    print("uusi", uusi_lista)
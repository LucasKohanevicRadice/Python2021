# tee ratkaisu tänne

def tee_tuple(x: int, y:int, z: int):

    lista = [x,y,z]
    lista.sort()

    pienin = lista[0]
    suurin = lista[-1]
    summa = sum(lista)

    # tupu = (pienin, suurin, summa)

    return (pienin, suurin, summa)


if __name__ == "__main__":
    print(tee_tuple(5, 3, -1))


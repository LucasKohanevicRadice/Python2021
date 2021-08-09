# tee ratkaisu tänne


def uniikit(lista : list):

    lista.sort()
    lista2 = []

    for luku in lista:
        if luku not in lista2:
            lista2.append(luku)

    return lista2


if __name__ == "__main__":
    
    lista = [1,2]
    print(uniikit(lista)) # [1, 2, 3]
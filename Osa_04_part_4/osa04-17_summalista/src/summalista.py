# tee ratkaisu tänne


def summa(lista1 : list, lista2 : list):

    lista3 = []

    for i in range(0,len(lista1)):
        lista3.append(lista1[i] + lista2[i])
    
    return lista3


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]

    print(summa(a,b))

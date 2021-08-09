# TEE RATKAISUSI TÄHÄN:

def listaan_lukuja(lista:list):

    if len(lista) % 5 != 0:
        lista.append(lista[-1]+1)
        listaan_lukuja(lista)

if __name__ == "__main__":
    luvut = [1,3,4,5,10,11]
    listaan_lukuja(luvut)
    print(luvut)
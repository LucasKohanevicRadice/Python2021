# Kirjoita ratkaisu tähän


def alkioiden_lisäys_listaan():

    quantity = int(input("Anna lukujen määrä: "))
    i = 0
    lista = []

    while i < quantity:
        value = int(input("Anna luku: "))
        lista.append(value) #Append-metodilla saadaan suoraan lisättyä, arvoja listaan.
        i += 1
    print(lista)

alkioiden_lisäys_listaan()

# Kirjoita ratkaisu tähän

def alkioiden_arvojen_muutokset():
    lista = [1, 2, 3, 4, 5]

    while True:

        index = int(input("Anna indeksi: "))
        if index == -1:
            break
        new_value = int(input("Anna arvo: "))
        lista[index] = new_value
        print(lista)



alkioiden_arvojen_muutokset()

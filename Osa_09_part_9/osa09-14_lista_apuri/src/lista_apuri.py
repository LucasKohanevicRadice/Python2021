# TEE RATKAISUSI TÄHÄN:
class ListaApuri:

    @classmethod
    def suurin_frekvenssi(cls,lista: list):
        return max(set(lista), key = lista.count)
    
    @classmethod
    def tuplia(cls,lista:list):
        i = 0
        for indeksi, alkio in enumerate(lista):
            if lista.count(alkio) >= 2:
                i += 1
            lista.pop(indeksi)
                
        return i


if __name__ == "__main__":
    luvut = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]

    print(ListaApuri.suurin_frekvenssi(luvut))
    print(ListaApuri.tuplia(luvut))

    # eniten = max(set(lista), key= lista.count)
    # print(eniten)


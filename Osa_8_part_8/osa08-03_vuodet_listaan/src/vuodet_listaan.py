# tee ratkaisu tänne
# Muista import-lause:
# from datetime import date

from datetime import date

def vuodet_listaan(vuodet: list):

    uusilista = []

    for pvm in vuodet:
        vuodet = pvm.year
        uusilista.append(vuodet)
    
    uusilista.sort()

    return uusilista
    
    

if __name__ == "__main__":
    p1 = date(2020,2, 12)
    p3 = date(1999,12, 4)
    p2 = date(2002,4, 17)

    lista = [p1,p2,p3]

    print(vuodet_listaan(lista))








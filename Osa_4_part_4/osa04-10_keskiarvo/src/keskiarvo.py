# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti

def keskiarvo(lista):

    ka = sum(lista) / len(lista)
    return ka

if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = keskiarvo(lista) 
    print(tulos)

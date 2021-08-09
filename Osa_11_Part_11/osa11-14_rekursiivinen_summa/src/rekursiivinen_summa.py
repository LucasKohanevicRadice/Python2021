# TEE RATKAISUSI TÄHÄN:

def summa(luku:int):

    if luku <= 1:
        return luku
    
    alempien_lukujen_summa = 0

    i = luku
    while i-1 > 0:
        alempien_lukujen_summa += i-1
        i -= 1
    return alempien_lukujen_summa + luku
if __name__ == "__main__":
    print(summa(3))
    print(summa(5))
    print(summa(10))
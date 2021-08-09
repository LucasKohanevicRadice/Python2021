# tee ratkaisu tänne

def laske_alkiot(matriisi: list, alkio:int):

    maara = 0

    for i in range(0,1):

        for lista in matriisi:
            for alkkis in lista:
                if alkkis == alkio:
                    maara += 1
    
    return maara





if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(laske_alkiot(m, 1))
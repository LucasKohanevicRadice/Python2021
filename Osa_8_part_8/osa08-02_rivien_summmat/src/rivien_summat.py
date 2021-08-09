# tee ratkaisu tänne

def rivien_summat(matriisi: list):

    for rivi in matriisi:
        rivi.append(sum(rivi))
    
    




if __name__ == "__main__":
    matriisi = [
    [1,3,5,6,8,3,5],
    [5,7,4,8,2,4,8],
    [1,4,5,3,6,0,5],
    [2,1,6,8,4,9,3]
    ]

    print(matriisi)

    rivien_summat(matriisi)

    print(matriisi)

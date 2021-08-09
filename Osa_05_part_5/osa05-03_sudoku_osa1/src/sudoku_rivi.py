# tee ratkaisu tänne
from typing import Counter

def rivi_oikein(sudoku: list, rivi_nro: int):

    rivi = sudoku[rivi_nro]
    laskin = Counter(rivi)
    laskettavat = [1,2,3,4,5,6,7,8,9]

    verification = True

    for avain, alkio in laskin.items():

        if avain == 0:
            continue

        if alkio > 1:

            verification = False
    
    return verification










if __name__ == "__main__":   



    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    

    # print(rivi_oikein(sudoku, 0))
    # print(rivi_oikein(sudoku, 1))
    # print(rivi_oikein(sudoku,2))



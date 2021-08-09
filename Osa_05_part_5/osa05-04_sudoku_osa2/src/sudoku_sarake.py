# tee ratkaisu tänne

from typing import Counter


def sarake_oikein(sudoku: list, sarake_nro: int):

    sarake = []
    verification = True
    

    for rivi in sudoku:
        sarake.append(rivi[sarake_nro])
    
    laskin = Counter(sarake)
    
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

    print(sarake_oikein(sudoku, 0))
    print(sarake_oikein(sudoku, 1))

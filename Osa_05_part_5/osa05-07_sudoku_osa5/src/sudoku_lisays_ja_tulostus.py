# tee ratkaisu tänne






def lisays(sudoku: list, rivi_nro: int, sarake_nro: int, luku: int):


    sudoku[rivi_nro][sarake_nro] = luku


    return sudoku

    

    


def tulosta(sudoku: list):

    muotoiltava = sudoku

    i = 0

    for rivi in muotoiltava:

        for index, item in enumerate(rivi):

            # if i % 3 == 0:
            #     print("  ")
            
            # else:
            #     print(" ")

            if item == 0:

                rivi[index] = "_"
            
            if i % 3 == 0:
                print("  ")
            
            else:
                print(" ")
    
    for rivi in muotoiltava:
        print(rivi)
    



    



sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


tulosta(sudoku)
lisays(sudoku, 0, 0, 2)
lisays(sudoku, 1, 2, 7)
lisays(sudoku, 5, 7, 3)
print()
print("Kolme numeroa lisätty:")
print()
tulosta(sudoku)



#   Enumerate esim

# sudoku  = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]



# for rivi in sudoku:

#     for index, item in enumerate(rivi):

#         if item == 0:
#             rivi[index] = "_"

# print(sudoku)
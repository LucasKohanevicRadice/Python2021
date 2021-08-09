# tee ratkaisu tänne

# def poista_pienin(luvut: list):

#     uusilista = []
#     for alkio in luvut:
#         uusilista.append(alkio)

#     uusilista.remove(min(uusilista))
#     luvut[:] = uusilista



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



for rivi in sudoku:

    for index, item in enumerate(rivi):

        if item == 0:
            rivi[index] = "_"


for rivi in sudoku:
    print(rivi)
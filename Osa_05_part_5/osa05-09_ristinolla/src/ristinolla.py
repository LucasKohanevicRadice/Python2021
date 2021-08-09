# tee ratkaisu tänne

def pelaa_siirto(lauta: list, x: int, y: int, nappula: str):

    #   Tapa 1:

    # if x not in range(0,2):
    #     return False

    # if y not in range(0,2):
    #     return False
    
    # if lauta[y][x] != "":
    #     return False

    # if nappula != "X" or nappula != "O":
    #     return False
    
    
    # lauta[y][x] = nappula
    # return True


    # Tapa 2:

    # if x not in range(0,2):
    #     return False

    # elif y not in range(0,2):
    #     return False
    
    # elif lauta[y][x] != "":
    #     return False

    # elif nappula != "X" or nappula != "O":
    #     return False
    
    
    # lauta[y][x] = nappula
    # return True

    #   Tapa 3:

    verification = False

    if x in range(0,3) and y in range(0,3):

        if lauta[y][x] == "":

            if nappula == "X" or nappula == "O":

                lauta[y][x] = nappula
                verification = True


    return verification







if __name__ == "__main__":

    lauta = [["", "", ""], ["", "", ""], ["", "", ""]]

    print(pelaa_siirto(lauta, 2, 0, "X"))
    print(lauta)
    print(pelaa_siirto(lauta, 1, 0, "X"))
    print(lauta)
    print(pelaa_siirto(lauta, 1, 0, "X"))
    print(lauta)











# def pelaa_siirto(lauta: list, x: int, y: int, nappula: str):

#     if x and y not in range(0,2):
#         return False
#     # if x < 0 or y < 0 or x > 2 or y > 2:
#     #     return False



#     if lauta[y][x] == "":
#         lauta[y][x] = nappula
#         # for rivi in lauta:
#         #     print(rivi)
#         return True, lauta

#     else:
#         return False
















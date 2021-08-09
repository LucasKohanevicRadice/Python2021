# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti




def samat(sana, x, y):

    if x >= len(sana) and x != y:
        return False

    elif y >= len(sana) and x != y:
        return False

    elif sana[x] == sana[y]:
        return True

    elif sana[x] != sana[y]:
        return False

#     # elif x > len(sana):
#     #     return False
#     #
#     # elif y > len(sana):
#     #     return False
#
#
#
#
if __name__ == "__main__":
    print(samat("abc", 3, 3))




if __name__ == "__main__":
    print(samat("koodari", 1, 2)) 
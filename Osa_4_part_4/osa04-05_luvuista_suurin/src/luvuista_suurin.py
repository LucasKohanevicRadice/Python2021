# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti

def luvuista_suurin(x, y, z):

    lst = [x, y, z]

    return max(lst)

    # if x > y and x > z:
    #     return x

    # elif y > x and y > z:
    #     return y

    # elif z > x and z > y:
    #     return z

    # elif x == z and x == y:
    #     return x


if __name__ == "__main__":
    suurin = luvuista_suurin(1, 2, 5)




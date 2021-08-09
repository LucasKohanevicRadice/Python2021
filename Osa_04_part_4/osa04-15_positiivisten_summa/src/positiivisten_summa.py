# tee ratkaisu tänne


def positiivisten_summa(lista : list):

    positiiviset = []

    for num in lista:
        if num > 0:
            positiiviset.append(num)
    
    return sum(positiiviset)


# print(positiivisten_summa([1, -1, 2, -2, 3, -3]))
if __name__ == "__main__":

    vastaus = positiivisten_summa([1, -1, 2, -2, 3, -3])
    print("vastaus", vastaus)



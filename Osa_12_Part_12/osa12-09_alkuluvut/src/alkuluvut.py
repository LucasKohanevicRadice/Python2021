# TEE RATKAISUSI TÄHÄN:


def alkuluvut(): 

    luku = 0 

    while True:
        if luku >= 2 and luku % 1 == 0 and luku % luku == 0: 
            yield luku
            luku += 1

        else:
            luku += 1


if __name__ == "__main__":

    luvut = alkuluvut()

    for i in range(8):
        print(next(luvut))

    #   Ei mee kaaliin



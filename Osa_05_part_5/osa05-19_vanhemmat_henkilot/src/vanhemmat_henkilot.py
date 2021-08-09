# tee ratkaisu tänne


def vanhemmat(henkilot: list, vuosi: int):

    herranvuodet = []

    for hlot in henkilot:
        if hlot[1] < vuosi:
            herranvuodet.append(hlot[0])
    return herranvuodet

#foken wöööks
if __name__ == "__main__":
    h1 = ("Arto", 1977)
    h2 = ("Einari", 1985)
    h3 = ("Maija", 1953)
    h4 = ("Essi", 1997)
    hlista = [h1, h2, h3, h4]
    vanhemmat(hlista, 2000)
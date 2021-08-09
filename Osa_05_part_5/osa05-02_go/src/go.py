# tee ratkaisu tänne


def kumpi_voitti(pelilauta: list):

    ykkönen = 0
    kakkonen = 0


    for i in range(0,1):

        for rivi in pelilauta:
            for nappula in rivi:

                if nappula == 1:
                    ykkönen += 1

                elif nappula == 2:
                    kakkonen += 1


    if ykkönen > kakkonen:
        return 1
    elif kakkonen > ykkönen:
        return 2
    elif ykkönen == kakkonen:
        return 0



if __name__ == "__main__":

    go = [[1,2,1,0],
        [1,1,2,2],
        [2,1,1,0]]


    print(kumpi_voitti(go))



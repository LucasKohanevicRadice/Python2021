# tee ratkaisu tänne



from fractions import Fraction


def jaa_palasiksi(maara: int):

    import fractions

    lesti = []

    murtoluku = Fraction(1, maara)

    # i = 0
    # while i != maara:
    for i in range(maara):
        lesti.append(murtoluku)
        # i += 1
    
    print(lesti)



    return murtoluku


# jaa_palasiksi(8)


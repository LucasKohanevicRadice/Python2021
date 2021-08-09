
def sulut_tasapainossa(merkkijono: str):

    sallitut = "{}[]()"
    aalto = "{}"
    haka = "[]"
    sulkeet = "()"


    if len(merkkijono) == 0:
        return True
    
    for kirjain in merkkijono:
        if kirjain not in sallitut:
            merkkijono = merkkijono.replace(kirjain, "")
    
    if not (merkkijono[0] == sulkeet[0] and merkkijono[-1] == sulkeet[1]):
        return False

    elif not (merkkijono[0] == haka[0] and merkkijono[-1] == haka[1]):
        return False
    
    elif not (merkkijono[0] == aalto[0] and merkkijono[-1] == aalto[1]):
        return False
    

    # poistetaan ensimmäinen ja viimeinen merkki
    return sulut_tasapainossa(merkkijono[1:-1])


if __name__ == "__main__":
    ok = sulut_tasapainossa("([([])])")
    print(ok)

    ok = sulut_tasapainossa("(python versio [3.7]) käytä tätä!")
    print(ok)

    # ei kelpaa sillä virheellinen loppusulku
    ok = sulut_tasapainossa("(()]")
    print(ok)


    # ei kelpaa sillä erityyppiset sulut menevät ristiin
    ok = sulut_tasapainossa("([huono)]")
    print(ok)



    # sallitut = "{}[]()"
    # merkkijono = "(perseen-nuolentakilpailu[]{})"

    # for kirjain in merkkijono:
    #     if kirjain not in sallitut:
    #         merkkijono = merkkijono.replace(kirjain, "")
    # print(merkkijono)

    #This how we do it


    #   Emmää saatan osaa
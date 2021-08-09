# tee ratkaisu tänne


import string

def vaihda_koko(merkkijono: str):

    uusi = ""

    for kirjain in merkkijono:
        if kirjain == kirjain.lower():
            kirjain = kirjain.upper()
            uusi += kirjain

        elif kirjain == kirjain.upper():
            kirjain = kirjain.lower()
            uusi += kirjain
        
        elif kirjain == " ":
            uusi += kirjain
    
    return uusi

def puolita(merkkijono: str):

    ekapuoli = ""
    tokapuoli = ""
    jako = len(merkkijono) // 2

    ekapuoli += merkkijono[:jako]
    tokapuoli += merkkijono[jako:]
    

    return ekapuoli, tokapuoli


def poista_erikoismerkit(merkkijono:str):

    # Jos et jaksa luetella kiellettyjä, kerro vaan sallitut:

    uusi = ""

    sallitut = string.ascii_letters + string.digits + "ÄäÅåÖö" + " "

    for kirjain in merkkijono:
        if kirjain in sallitut:
            uusi += kirjain
        else:
            continue
    return uusi





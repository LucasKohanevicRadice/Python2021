# tee ratkaisu tänne

from difflib import get_close_matches
import string

def spellchecker_v2():

    for i in range(1,3):
        print()
    syote = input("Write a text in english: ")
    syote = syote.lower()

    korjattusyote = ""
    sanalista = []

    with open("Top_picks\osa07-16_spellchecker_versio2\src\wordlist.txt") as tiedosto:

        for rivi in tiedosto:
            rivi = rivi.strip()
            rivi = rivi.lower()
            sanalista.append(rivi)
    
    sanat = syote.split(" ")

    korjauskehotus = f"korjausehdotukset: \n"
    

    for sana in sanat:
        if sana not in sanalista:
            vääräsana = sana
            korjattusyote += f"*{vääräsana}*" + " "
            korjauskehotus += f"{vääräsana}: {get_close_matches(vääräsana,sanalista, n=5)}\n"

        else:
            korjattusyote += sana + " "
    korjattusyote = korjattusyote.strip()

    print()
    print(korjattusyote)
    print()
    print(korjauskehotus)


spellchecker_v2()

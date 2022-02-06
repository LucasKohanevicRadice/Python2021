# tee ratkaisu tänne

from difflib import get_close_matches
import string

def spellchecker_v2():

    print()
    syote = input("Write a text in english: ")
    syote = syote.lower()

    korjattusyote = ""
    korjauskehotus = f"korjausehdotukset: \n"
    sanalista = []

    with open("Top_picks\osa07-16_spellchecker_versio2\src\wordlist.txt") as tiedosto:

        for rivi in tiedosto:
            rivi = rivi.strip()
            rivi = rivi.lower()
            sanalista.append(rivi)
    
    sanat = syote.split(" ")
  

    for sana in sanat:
        if sana not in sanalista:
            vääräsana = sana
            korjattusyote += f"*{vääräsana}*" + " "
            korjauskehotus += f"{vääräsana}: {get_close_matches(vääräsana,sanalista, n=5)}\n"

        else:
            korjattusyote += sana + " "


    print()
    print(korjattusyote)
    print()
    print(korjauskehotus)
    print()



spellchecker_v2()

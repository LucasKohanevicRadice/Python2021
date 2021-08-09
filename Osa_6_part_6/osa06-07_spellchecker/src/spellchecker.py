# tee ratkaisu tänne
def spellchecker():
    sanalista = []

    with open ("wordlist.txt") as tiedosto:
        for sana in tiedosto:
            sana = sana.replace("\n", "")
            sanalista.append(sana)


    output = ""
    sentence = input("Write text: ")
    # sentence = sentence.lower()
    sentence = sentence.split()

    for sana in sentence:

        if sana.lower() not in sanalista:
            sana = sana.replace(sana, f"*{sana}*")
        
        if len(output) == 0:
            output += sana
        else:
            output += " " + sana

    print(output)


spellchecker()

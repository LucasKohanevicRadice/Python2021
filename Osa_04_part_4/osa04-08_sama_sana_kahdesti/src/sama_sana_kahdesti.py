# Kirjoita ratkaisu tähän


def sama_sana_kahdesti():

    list = []
    i = 0
    while True:

        word = input("sana: ")

        if word in list:
            print(f"Annoit {i} eri sanaa")
            break

        else:
            list.append(word)
            i += 1
        

sama_sana_kahdesti()

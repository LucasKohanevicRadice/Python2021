# Kirjoita ratkaisu tähän


def lista_kahdesti():

    list = []

    while True:

        value = int(input("Anna luku: "))
        if value == 0:
            print("Moi!")
            break
        else:
            list.append(value)
            print(f"Lista: {list}")
            print(f"Järjestettynä: {sorted(list)}")



lista_kahdesti()


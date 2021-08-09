# Kirjoita ratkaisu tähän




def lisäys_poisto():

    list = []
    i = 0
    while True:
        print("Lista on nyt", list)
        choice = input("(l)isää, (p)oista vai e(x)it: ")

        if choice == "l":
            i += 1
            list.append(i)

        elif choice == "p":
            list.remove(i)
            i -= 1

        elif choice == "x":
            print("Moi!")
            break


lisäys_poisto()
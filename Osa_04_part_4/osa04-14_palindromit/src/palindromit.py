# tee ratkaisu tänne
# huomaa, että tällä kertaa pääohjelmaa ei tule kirjoittaa lohkon
# if __name__ == "__main__":
# sisälle!


def palindromi(m1: str):

    if m1[0:] == m1[::-1]:
        return True
    else:
        return False

while True:

    sana = input("Anna sana: ")

    if palindromi(sana) == True:
        print(f"{sana} on palindromi!")
        break
    
    elif palindromi(sana) == False:
        print(f"ei ollut palindromi")


from random import randint


class abc:

    def __init__(self) -> None:

        self.olio = []
        self.x = randint(1,7)

    
    def tulosta(self):
        print("persesess")
    

    # def palauta_olio(self):

    #     self.olio = []

    #     return self.olio

olio1 = abc().olio
olio2 = abc().olio

olio1.append("perse")
olio2.append("jeejee")

# print(olio1)
# print(olio2)
# print(olio1)

ollie1 = abc()

ollie2 = abc()

print(ollie1.x)
print(ollie2.x)




ollie1.tulosta()
# Tee ratkaisusi tähän:
import datetime

class Sekuntikello:

    def __init__(self, tunnit: int, minuutit: int, sekunnit: int):

        self.aloitusaika = datetime.datetime(1,1,1,tunnit,minuutit,sekunnit)
        aloitusaika = self.aloitusaika
        self.sekuntti = datetime.timedelta(seconds=1)
        sekuntti = self.sekuntti
        

    def tick(self):

        self.aloitusaika += self.sekuntti
    
    def aseta(self, tunnit: int, minuutit: int):
        self.aloitusaika = datetime.datetime(1,1,1,tunnit,minuutit,0)

    
    def __str__(self) -> str:
        return self.aloitusaika.strftime("%H:%M:%S")



kello = Sekuntikello()
for i in range(3600):
    print(kello)
    kello.tick()



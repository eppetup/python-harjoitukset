import random

class Auto:
    def __init__ (self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinenNopeus = 0
        self.kuljettuMatka = 0

    def kiihdyta(self, nopeudenMuutos):

        if nopeudenMuutos + self.tamanhetkinenNopeus < 0:
            self.tamanhetkinenNopeus = 0
            return

        if nopeudenMuutos + self.tamanhetkinenNopeus > self.huippunopeus:
            self.tamanhetkinenNopeus = self.huippunopeus
            return

        self.tamanhetkinenNopeus += nopeudenMuutos

    def kulje(self, tunnit):

        self.kuljettuMatka += tunnit * self.tamanhetkinenNopeus

    
class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for x in self.autot:
             x.kiihdyta(random.randint(-10, 15))
             x.kulje(1)

    def tulosta_tilanne(self):
        rekisteritunnukset = "Rekisteritunnukset: "
        huippunopeudet = "Huippunopeudet: "
        tamanhetkisetNopeudet = "Tämänhetkiset nopeudet: "
        kuljetutMatkat = "Kuljetut matkat: "

        for x in self.autot:
            rekisteritunnukset += str(x.rekisteritunnus) + " "
            huippunopeudet += str(x.huippunopeus) + " "
            tamanhetkisetNopeudet += str(x.tamanhetkinenNopeus) + " "
            kuljetutMatkat += str(x.kuljettuMatka) + " "

        print (rekisteritunnukset)
        print (huippunopeudet)
        print (tamanhetkisetNopeudet)
        print (kuljetutMatkat)
        print("\n")

    def kilpailu_ohi(self):
        for x in self.autot:
            if x.kuljettuMatka >= self.pituus:
                return True
        return False


# main
listaAutoista = []

for x in range(10):
  listaAutoista.append(Auto(f"ABC-{x+1}", random.randint(100, 200)))

kilpailu = Kilpailu("Suuri romuralli", 8000, listaAutoista)

tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    kilpailu.kilpailu_ohi()
    tunti += 1
    if tunti % 10 == 0:
        kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()
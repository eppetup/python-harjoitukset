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


def tulostaTiedot(autot):

    rekisteritunnukset = "Rekisteritunnukset: "
    huippunopeudet = "Huippunopeudet: "
    tamanhetkisetNopeudet = "Tämänhetkiset nopeudet: "
    kuljetutMatkat = "Kuljetut matkat: "

    for x in autot:
        rekisteritunnukset += str(x.rekisteritunnus) + " "
        huippunopeudet += str(x.huippunopeus) + " "
        tamanhetkisetNopeudet += str(x.tamanhetkinenNopeus) + " "
        kuljetutMatkat += str(x.kuljettuMatka) + " "

    print (rekisteritunnukset)
    print (huippunopeudet)
    print (tamanhetkisetNopeudet)
    print (kuljetutMatkat)
    


# main
listaAutoista = []

for x in range(10):
  listaAutoista.append(Auto(f"ABC-{x+1}", random.randint(100, 200)))

# kilpailu
eiVoittajaa = True
while eiVoittajaa:
    
    for x in listaAutoista:

        x.kiihdyta(random.randint(-10, 15))
        x.kulje(1)

        if x.kuljettuMatka >= 10000:
            eiVoittajaa = False
            break

tulostaTiedot(listaAutoista)
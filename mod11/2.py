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

class Sähköauto(Auto):
    def __init__ (self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__ (self, rekisteritunnus, huippunopeus, bensatankinKoko):
        super().__init__(rekisteritunnus, huippunopeus)

# main

sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sähköauto.kiihdyta(100)
polttomoottoriauto.kiihdyta(160)

sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"{sähköauto.kuljettuMatka}km")
print(f"{polttomoottoriauto.kuljettuMatka}km")
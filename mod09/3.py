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


# main
uusiAuto = Auto("ABC-123", 142)

print(f"rekisteritunnus: {uusiAuto.rekisteritunnus}")
print(f"huippunopeus: {uusiAuto.huippunopeus} km/h")
print(f"tämänhetkinen nopeus: {uusiAuto.tamanhetkinenNopeus} km/h")
print(f"kuljettu matka: {uusiAuto.kuljettuMatka} km")

# kiihdytys
uusiAuto.kiihdyta(30)
uusiAuto.kiihdyta(70)
uusiAuto.kiihdyta(50)
print(f"tämänhetkinen nopeus: {uusiAuto.tamanhetkinenNopeus} km/h")

# hätäjarrutus
uusiAuto.kiihdyta(-200)
print(f"tämänhetkinen nopeus: {uusiAuto.tamanhetkinenNopeus} km/h")

# kulje test
uusiAuto.kuljettuMatka = 2000
uusiAuto.tamanhetkinenNopeus = 60
uusiAuto.kulje(1.5)
print(f"kuljettu matka: {uusiAuto.kuljettuMatka} km")
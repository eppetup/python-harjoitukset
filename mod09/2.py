class Auto:
    def __init__ (self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinenNopeus = 0
        self.kuljettuMatka = 0

# main
uusiAuto = Auto("ABC-123", "142")

print(f"rekisteritunnus: {uusiAuto.rekisteritunnus}")
print(f"huippunopeus: {uusiAuto.huippunopeus} km/h")
print(f"tämänhetkinen nopeus: {uusiAuto.tamanhetkinenNopeus} km/h")
print(f"kuljettu matka: {uusiAuto.kuljettuMatka} km")

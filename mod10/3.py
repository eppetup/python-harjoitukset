class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerrosNyt = alin

    def siirry_kerrokseen(self, kerros):
        while(self.kerrosNyt < kerros):
            self.kerros_ylös()
        while(self.kerrosNyt > kerros):
            self.kerros_alas()       
            
    def kerros_ylös(self):
        self.kerrosNyt += 1
        print(f"Hissi on kerroksessa {self.kerrosNyt}")
    def kerros_alas(self):
        self.kerrosNyt -= 1
        print(f"Hissi on kerroksessa {self.kerrosNyt}")

class Talo:
    def __init__(self, alin, ylin, hissienMaara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for x in range(hissienMaara):
            self.hissit.append(Hissi(alin, ylin))
    def aja_hissiä(self, hissi, kerros):
        self.hissit[hissi].siirry_kerrokseen(kerros)
    def palohalytys(self):
        for x in self.hissit:
          x.siirry_kerrokseen(self.alin)



# main
talo = Talo(1,10,4)
talo.aja_hissiä(1,4)
talo.aja_hissiä(2,5)

talo.palohalytys()

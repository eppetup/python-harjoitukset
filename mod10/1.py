class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerrosNyt = alin

    def siirry_kerrokseen(self, kerros):
        if (self.kerrosNyt < kerros):
            for x in range (kerros - self.kerrosNyt):
                self.kerros_ylös()
        if (self.kerrosNyt > kerros):
             for x in range (self.kerrosNyt - kerros):
                 self.kerros_alas()       
            
    def kerros_ylös(self):
        self.kerrosNyt += 1
        print(f"Hissi on kerroksessa {self.kerrosNyt}")
    def kerros_alas(self):
        self.kerrosNyt -= 1
        print(f"Hissi on kerroksessa {self.kerrosNyt}")

# main
hissi = Hissi(1,10)
hissi.siirry_kerrokseen(4)
hissi.siirry_kerrokseen(2)
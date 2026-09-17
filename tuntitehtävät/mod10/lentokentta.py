class Lentokone:
    def __init__(self, id, bensaMax, bensaNow):
        self.id = id
        self.bensaMax = bensaMax
        self.bensaNow = bensaNow

    def tankkaa(self):
        print(f"Bensaa mahtui {self.bensaMax - self.bensaNow}")
        self.bensaNow = self.bensaMax
        return

    def tulosta_tiedot(self):
        print(f"Nimi: {self.id}")
        print(f"Bensatankin maksimi: {self.bensaMax}") 
        print(f"Bensatankin nykyinen lukema: {self.bensaNow}")
        return

class Lentokenttä:
    def __init__(self, id):
        self.id = id
        self.koneet = []

    def tulosta_koneet(self):
        for x in self.koneet:
            x.tulosta_tiedot()

    def lisaa_kone(self, kone):
        self.koneet.append(kone)

kone1 = Lentokone("Timo", 100, 50)
kone2 = Lentokone("Juuso", 50, 25)

kentta = Lentokenttä("Kentta")

kentta.lisaa_kone(kone1)
kentta.lisaa_kone(kone2)

kentta.tulosta_koneet()

kone1.tankkaa()

kentta.tulosta_koneet()


            
    
ROSKAKORIT = ["muovi","bio","metalli","sekajäte"]

class Pelaaja:
    def __init__ (self, nimi, huone):
        self.nimi = nimi
        # pelaajan keräämät tavarat
        self.tavarat = []
        # alussa 0 pistettä
        self.pisteet = 0
        self.huone = huone

    # liikkuu huoneeseen
    def liiku(self, huone):
        self.huone = huone

    # kerää esine
    def keraaEsine(self, esine):
        self.tavarat.append(esine)
        self.huone.esineet.remove(esine)
        print(f"Keräsit esineen: {esine.nimi}")
        self.lajittele(esine)
    # tulosta pisteiden määrä
    def tulostaPisteet(self):
        print("Pisteitä on: ")
        print (self.pisteet)
    # kysytään oikeaa roskakoria
    def lajittele(self, esine):
        print(f"\nMihin roskakoriin '{esine.nimi}' kuuluu?")
        print(", ".join(ROSKAKORIT))
        while True:
            vastaus = input("> ")
            if vastaus in ROSKAKORIT:
                break
        if vastaus == esine.roskakori:
            self.pisteet += 1
            print("Oikein! +1 piste")
        else:
            print(f"Väärin. Oikea roskakori olisi: {esine.roskakori}")        

class Huone:
    def __init__ (self, nimi, esineet):
        self.nimi = nimi
        self.esineet = [esineet]
        self.seuraava = None

class Esine:
    def __init__ (self, nimi, roskakori):
        self.nimi = nimi
        self.roskakori = roskakori

    
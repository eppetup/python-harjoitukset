class Pelaaja:
    def __init__ (self, nimi, huone):
        self.nimi = nimi
        self.tavarat = []
        self.huone = huone
   
    def liiku(self, huone):
        self.huone = huone
  
    def keraaEsine(self, esine):
        if esine in self.huone.esineet:
            self.tavarat.append(esine)
            self.huone.esineet.remove(esine)
            print(f"Keräsit esineen: {esine.nimi}")
        else:
            print(f"Esine {esine.nimi} ei ole tässä huoneessa.")
    
    def tulostaTavarat(self):
        print("Laukussa on: ")
        for x in self.tavarat:
            print(f"- {x.nimi}, {x.paino} kg")

class Huone:
    def __init__ (self, nimi, esineet):
        self.nimi = nimi
        self.esineet = [esineet]
        self.seuraava = None

class Esine:
    def __init__ (self, nimi, paino):
        self.nimi = nimi
        self.paino = paino
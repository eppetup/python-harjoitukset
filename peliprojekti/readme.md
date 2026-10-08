siivouspeli

pelissä seikkaillaan huoneissa, joissa on erilaisia roskia.
kerätyt roskat tulee lajitella oikeaan roskakoriin: muovi, bio, metalli, sekajäte
pisteitä kerätään tekemällä oikeita valintoja (maksimipisteet 4).
valittuaan väärin pelaajalle paljastetaan oikea vastaus.
pisteet voi tarkistaa pelin aikana, ja ne näytetään myös pelin lopussa.

peli liittyy kestävän kehityksen tavoitteeseen 12, jossa mainitaan jätteiden oikea lajittelu.
oikeanlainen lajittelu mahdollistaa kierrätyksen, jolla säästetään luonnonvaroja.

keräämättä jätetyistä esineistä ei saa pisteitä.

kun ohjelma käynnistetään, kysyy se pelaajalta iän ja nimen. peli on tarkoitettu yli 12-vuotiaille.
tämän jälkeen tulostetaan tekstitiedostojen intro.txt ja ohjeet.txt -sisällöt.

päävalikossa on 5 vaihtoehtoa:
    1. pelaa: käynnistää pelin
    2. tallenna: tallentaa pelin tilan tiedostoon tallennus.txt
    3. historia: tulostaa pelaajan antamat komennot
    4. asetukset: pelin nollaus
    5. lopeta: lopettaa ohjelman

pelin aikana on 4 vaihtoehtoa:
    1. liiku: siirtyy seuraavaan huoneeseen
    2. poimi: poimii roskan, ja kysyy oikeaa roskakoria
    3. pisteet: tulostaa pistetilanteen
    4. valikko: palaa päävalikkoon


tiedostojen rakenne

ohjelma.py: ohjelman käynnistys, esineiden ja huoneiden luonti, päävalikko

funktiot.py: ohjelmassa käytettävät funktiot: 
    alaikatest()
    tulostaIntro()
    tulostaOhjeet()
    pelaa(lista, pelaaja)
    tallenna(pelaaja)
    lataaTallennus(pelaaja, huoneet)
    historia(lista)
    asetukset(pelaaja, huoneet, esineet)
    lopeta()

luokat.py: ohjelmassa käytettävät luokat
    Pelaaja
    Huone
    Esine


tunnetut ongelmat:
- vain yhden ihmisen peli voidaan tallentaa
- virheellinen syöte voi kaataa ohjelman


    







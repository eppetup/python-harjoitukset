import funktiot
import luokat

funktiot.alaikatest()
funktiot.tulostaIntro()
input()
funktiot.tulostaOhjeet()
input()

# esineet
muoviroska = luokat.Esine("Muoviroska", "muovi")
banaani = luokat.Esine("Pilaantunut banaani", "bio")
juoma = luokat.Esine("Tyhjä juomatölkki", "metalli")
styroksi = luokat.Esine("Styroksinpala", "sekajäte")

# paikat
huone1 = luokat.Huone("kellari", muoviroska)
huone2 = luokat.Huone("olohuone", juoma)
huone3 = luokat.Huone("keittiö", banaani)
huone4 = luokat.Huone("eteinen", styroksi)

huone1.seuraava = huone2
huone2.seuraava = huone3
huone3.seuraava = huone4

esineet = [muoviroska, banaani, juoma, styroksi]
huoneet = [huone1, huone2, huone3, huone4]

nimi = input('Pelaajan nimi > ')
pelaaja = luokat.Pelaaja(nimi, huone1)
funktiot.lataaTallennus(pelaaja, huoneet)

lista = []

while(True):

    print(f'\nHei {nimi}!')
    print('Valitse toiminto:')
    print('\n  pelaa\n  tallenna\n  historia\n  asetukset\n  lopeta\n')

    syote = input('> ')

    match syote:
        case 'pelaa':
            funktiot.pelaa(lista, pelaaja)
        case 'tallenna':
            funktiot.tallenna(pelaaja)
        case 'historia':
            funktiot.historia(lista)
        case 'asetukset':
            funktiot.asetukset(pelaaja, huoneet, esineet)
        case 'lopeta':
            funktiot.lopeta()

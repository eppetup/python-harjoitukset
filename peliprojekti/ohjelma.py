import funktiot
import luokat

funktiot.alaikatest()
funktiot.tulostaIntro()
input()
funktiot.tulostaOhjeet()
input()

# esineet
vasara = luokat.Esine("Vasara", 4)
banaani = luokat.Esine("Banaani", 1)
kirja = luokat.Esine("Kirja", 1)
lappu = luokat.Esine("Lappu", 1)

# paikat
huone1 = luokat.Huone("kellari", vasara)
huone2 = luokat.Huone("olohuone", kirja)
huone3 = luokat.Huone("keittiö", banaani)
huone4 = luokat.Huone("eteinen", lappu)

huone1.seuraava = huone2
huone2.seuraava = huone3
huone3.seuraava = huone4

esineet = [vasara, banaani, kirja, lappu]
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

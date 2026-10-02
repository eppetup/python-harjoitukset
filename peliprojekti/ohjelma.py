import funktiot
import luokat

funktiot.alaikatest()

# esineet
vasara = luokat.Esine("Vasara", 4)
taskulamppu = luokat.Esine("Taskulamppu", 2)
kirja = luokat.Esine("Kirja", 1)

# huoneet
huone1 = luokat.Huone("1. huone", vasara)
huone2 = luokat.Huone("2. huone", kirja)
huone3 = luokat.Huone("3. huone", taskulamppu)

huone1.seuraava = huone2
huone2.seuraava = huone3
huone3.seuraava = huone1



nimi = input('Pelaajan nimi > ')
pelaaja = luokat.Pelaaja(nimi, huone1)

lista = []

while(True):

    print(f'\nHei {nimi}!')
    print('Valitse toiminto:')
    print('\n  pelaa\n  tulokset\n  asetukset\n  lopeta\n')

    syote = input('> ')

    match syote:
        case 'pelaa':
            funktiot.pelaa(lista, pelaaja)
        case 'tulokset':
            funktiot.tulokset(lista)
        case 'asetukset':
            funktiot.asetukset()
        case 'lopeta':
            funktiot.lopeta()

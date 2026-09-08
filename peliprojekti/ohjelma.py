def pelaa(lista):
    lista.append(input('Syötä sana > '))
    return

def tulokset(lista):
    print(lista)
    return

def asetukset():
    print('Työn alla')
    return

def lopeta():
    quit()



nimi = input('Pelaajan nimi > ')
ika = input('Pelaajan ikä > ')

if int(ika) < 12:
    print('Alaikä')
    quit()


lista = []

while(True):

    print(f'\nHei {nimi}!')
    print('Valitse toiminto:')
    print('\n  pelaa\n  tulokset\n  asetukset\n  lopeta\n')

    syote = input('> ')

    match syote:
        case 'pelaa':
            pelaa(lista)
        case 'tulokset':
            tulokset(lista)
        case 'asetukset':
            asetukset()
        case 'lopeta':
            lopeta()

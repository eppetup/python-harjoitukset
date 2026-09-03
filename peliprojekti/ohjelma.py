nimi = input('Pelaajan nimi > ')
ika = input('Pelaajan ikä > ')

if int(ika) < 12:
    print('Alaikä')
    quit()

while(True):

    print(f'\nHei {nimi}!')
    print('Valitse toiminto:')
    print('\n  pelaa\n  asetukset\n  lopeta\n')

    syote = input('> ')

    match syote:
        case 'pelaa':
            print('*** peli työn alla ***')
        case 'asetukset':
            print('*** asetukset työn alla ***')
        case 'lopeta':
            quit()

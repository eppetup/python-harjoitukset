import sys


def alaikatest():
    ika = input('Pelaajan ikä > ')
    if int(ika) < 12:
        print('Alaikä')
        sys.exit()


def pelaa(lista, pelaaja):

    while True:
        print(f"\nOlet huoneessa {pelaaja.huone.nimi}. Huoneessa on: ")
        if pelaaja.huone.esineet:
            for x in pelaaja.huone.esineet:
                print(f"- {x.nimi}")
        else:
            print("- Ei esineitä")

        print('\nValitse vaihtoehto: ')
        print('liiku, poimi esine, tavarat, valikko')
        valinta = input('> ').strip().lower()
        lista.append(valinta)

        match valinta:
            case 'liiku':
                pelaaja.liiku(pelaaja.huone.seuraava)
            case 'poimi esine':
                if pelaaja.huone.esineet:
                    pelaaja.keraaEsine(pelaaja.huone.esineet[0])
                else:
                    print("Huoneessa ei ole esineitä!")
            case 'tavarat':
                pelaaja.tulostaTavarat()
            case 'valikko':
                return

def tulokset(lista):
    print(lista)
    return

def asetukset():
    print('Työn alla')
    return

def lopeta():
    sys.exit()
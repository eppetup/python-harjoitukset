import sys

def alaikatest():
    ika = input('Pelaajan ikä > ')
    if int(ika) < 12:
        print('Alaikä')
        sys.exit()

def tulostaIntro():
    with open("intro.txt", 'r') as tiedosto:
        print(tiedosto.read())

def tulostaOhjeet():
    with open("ohjeet.txt", 'r') as tiedosto:
        print(tiedosto.read())



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


def tallenna(pelaaja):
    with open("tallennus.txt", 'w') as tiedosto:
        tiedosto.write(pelaaja.nimi + '\n')
        tiedosto.write(pelaaja.huone.nimi + "\n")
        tavarat = "\n".join([e.nimi for e in pelaaja.tavarat])
        tiedosto.write(tavarat + '\n')
        print("Tallennettu tiedostoon tallennus.txt")

def lataaTallennus(pelaaja, huoneet):
    try:
        with open("tallennus.txt", 'r') as tiedosto:
            rivit = [rivi.strip() for rivi in tiedosto.readlines()]
    except FileNotFoundError:
        return

    if rivit[0] != pelaaja.nimi:
        return
    
    print(f"Tervetuloa takaisin {pelaaja.nimi}")

    for huone in huoneet:
        if huone.nimi == rivit[1]:
            pelaaja.huone = huone
            break

    for tavara in rivit[2:]:
        if not tavara:
            continue
        for huone in huoneet:
            esine = next((e for e in huone.esineet if e.nimi == tavara), None)
            if esine:
                huone.esineet.remove(esine)
                pelaaja.tavarat.append(esine)
                break    

def tulokset(lista):
    print(lista)
    return

def asetukset():
    # reset game
    print('Työn alla')
    return

def lopeta():
    sys.exit()
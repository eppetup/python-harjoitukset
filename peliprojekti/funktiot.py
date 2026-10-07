import sys

# testaa onko pelaaja riittävän vanha
def alaikatest():
    ika = input('Pelaajan ikä > ')
    if int(ika) < 12:
        print('Alaikä')
        sys.exit()

# tulostaa intro.txt
def tulostaIntro():
    with open("intro.txt", 'r') as tiedosto:
        print(tiedosto.read())

# tulostaa ohjeet.txt
def tulostaOhjeet():
    with open("ohjeet.txt", 'r') as tiedosto:
        print(tiedosto.read())


# pelin toteutus
def pelaa(lista, pelaaja):

    while True:
        print(f"\nOlet huoneessa {pelaaja.huone.nimi}. Huoneessa on: ")
        if pelaaja.huone.esineet:
            for x in pelaaja.huone.esineet:
                print(f"- {x.nimi}")
        else:
            print("- Ei esineitä")

        print('\nValitse vaihtoehto: ')
        print('liiku, poimi, tavarat, valikko')
        valinta = input('> ').strip().lower()
        lista.append(valinta)

        match valinta:
            case 'liiku':
                if pelaaja.huone.seuraava is None:
                    print("Tämä on viimeinen paikka.")
                else:
                    pelaaja.liiku(pelaaja.huone.seuraava)
            case 'poimi':
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

def historia(lista):
    print(lista)
    return

def asetukset(pelaaja, huoneet, esineet):
    while True:
        print("Valitse vaihtoehto: \nnollaa peli, valikko")
        match input("> ").strip().lower():
            case "nollaa peli":
                for huone, esine in zip(huoneet, esineet):
                    huone.esineet = [esine]
                pelaaja.tavarat = []
                pelaaja.huone = huoneet[0]
                print("Peli nollattu.")
                break
            case "valikko":
                break

def lopeta():
    sys.exit()
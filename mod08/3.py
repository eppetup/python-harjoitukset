def uusiLentoasema():
  icao = input("Anna ICAO-koodi > ")
  nimi = input("Anna nimi > ")
  tiedot[icao] = nimi
  return

def haeTietoja():
    icao = input("Anna ICAO-koodi > ")
    print("\nLentoaseman nimi: " + tiedot[icao] + "\n")
    return

tiedot = {}

while True:

    print("Haluatko \n  1. Syottää uuden lentoaseman \n  2. Hakea tietoja\n  3. Lopettaa ")
    syote = input("Anna numero (1-3) > ")

    match syote:
        case "1":
            uusiLentoasema()
        case "2":
            haeTietoja()
        case "3":
            break
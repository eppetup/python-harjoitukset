while(True):

    tuumat = int(input("Anna tuumat > "))

    if tuumat < 0:
        quit()

    sentit = tuumat * 2.54

    print(f'{tuumat} tuumaa on {sentit} senttimetriä')

    
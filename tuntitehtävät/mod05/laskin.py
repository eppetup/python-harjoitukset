while(True):

    print("hei, tämä on laskin. valitse toiminto:")
    print("plus, miinus, kerto, seis")
    toiminto = input("> ")

    if toiminto == "seis":
        quit()

    luku1 = float(input("Anna 1. luku > "))
    luku2 = float(input("Anna 2. luku > "))

    if toiminto == "plus":
        print(f"\n{luku1} + {luku2} = {luku1 + luku2}\n")
    if toiminto == "miinus":
        print(f"\n{luku1} - {luku2} = {luku1 - luku2}\n")    
    if toiminto == "kerto":
        print(f"\n{luku1} * {luku2} = {luku1 * luku2}\n") 


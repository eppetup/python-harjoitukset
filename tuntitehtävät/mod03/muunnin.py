luku = int(input("Kuinka monta grammaa: "))

kilot = luku // 1000
grammat = luku % 1000

print(f"Määrä kiloina ja grammoina: {kilot} kg {grammat} g")
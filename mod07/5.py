def parittomatPois(luvut):
    parilliset = []
    for x in luvut:
        if x % 2 == 0:
            parilliset.append(x)
    return parilliset


luvut = [1,2,3,4,5,6,7,8,9,10]
print(f'alkuperäinen lista: {luvut}')
print(f'karsittu lista: {parittomatPois(luvut)}')

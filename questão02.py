def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media

notas = [8, 10, 9, 6]

media = calcular_media(notas)

print("A média das notas é:", media)

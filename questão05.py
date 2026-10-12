def notas_aprovadas(notas):
    aprovadas = []

    for nota in notas:
        if nota >= 7:
            aprovadas.append(nota)

    return aprovadas

notas = [8, 4, 9, 5, 6]

print(notas_aprovadas(notas))

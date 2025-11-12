import math


def suma_cuadrados(sumas):
    return sum(s * s for s in sumas)


def backtracking(i, habilidades, k, sumas, particion, mejor_valor, mejor_particion):

    sum_cuad_actual = suma_cuadrados(sumas)

    if sum_cuad_actual >= mejor_valor:
        return mejor_valor, mejor_particion

    if i == len(habilidades):
        if sum_cuad_actual < mejor_valor:
            mejor_valor = sum_cuad_actual
            mejor_particion = [list(g) for g in particion]
        return mejor_valor, mejor_particion

    valor, indice = habilidades[i]

    orden = sorted(range(k), key=lambda x: sumas[x])
    ya_uso_vacio = False  # para evitar permutaciones de los conjuntos
    for g in orden:
        if sumas[g] == 0:
            if ya_uso_vacio:
                continue
            ya_uso_vacio = True

        particion[g].append(indice)
        sumas[g] += valor

        mejor_valor, mejor_particion = backtracking(
            i + 1, habilidades, k, sumas, particion, mejor_valor, mejor_particion)

        sumas[g] -= valor
        particion[g].pop()

    return mejor_valor, mejor_particion


def resolver(k, habilidades):

    sumas = [0] * k
    particion = [[] for _ in range(k)]

    ordenadas = sorted(
        [(v, i) for i, v in enumerate(habilidades)], reverse=True)

    mejor_valor = math.inf
    mejor_particion = None

    return backtracking(
        0, ordenadas, k, sumas, particion, mejor_valor, mejor_particion)

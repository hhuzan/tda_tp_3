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

    # orden = sorted(range(k), key=lambda x: sumas[x])
    ya_uso_vacio = False  # para evitar permutaciones de los conjuntos
    # for g in orden:
    for g in range(k):
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


def resolver(k, habilidades, ordenar=True):

    tuplas = sorted([(v, i)
                     for i, v in enumerate(habilidades)], reverse=True) if ordenar else [(v, i) for i, v in enumerate(habilidades)]

    mejor_valor, mejor_particion = math.inf, None

    sumas = [0] * k
    particion = [[] for _ in range(k)]

    return backtracking(0, tuplas, k, sumas, particion, mejor_valor, mejor_particion)

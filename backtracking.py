import math


def backtracking(i, habilidades, k, sumas, sum_cuad_actual, particion, mejor_valor, mejor_particion):

    if sum_cuad_actual >= mejor_valor:
        return mejor_valor, mejor_particion

    if i == len(habilidades):
        if sum_cuad_actual < mejor_valor:
            mejor_valor = sum_cuad_actual
            mejor_particion = [list(g) for g in particion]
        return mejor_valor, mejor_particion

    valor, indice = habilidades[i]

    ya_uso_vacio = False  # para evitar algunas permutaciones de los conjuntos
    for g in range(k):
        if sumas[g] == 0:
            if ya_uso_vacio:
                continue
            ya_uso_vacio = True

        suma_anterior = sumas[g]

        incremento = (suma_anterior + valor) ** 2 - (suma_anterior ** 2)

        particion[g].append(indice)
        sumas[g] += valor
        sum_cuad_actual += incremento

        mejor_valor, mejor_particion = backtracking(
            i + 1, habilidades, k, sumas, sum_cuad_actual, particion, mejor_valor, mejor_particion)

        sumas[g] -= valor
        sum_cuad_actual -= incremento
        particion[g].pop()

    return mejor_valor, mejor_particion


def resolver(k, habilidades, ordenar=True):

    tuplas = sorted([(v, i)
                     for i, v in enumerate(habilidades)], reverse=True) if ordenar else [(v, i) for i, v in enumerate(habilidades)]

    mejor_valor, mejor_particion = math.inf, None

    sumas = [0] * k
    sum_cuad_actual = 0
    particion = [[] for _ in range(k)]

    return backtracking(0, tuplas, k, sumas, sum_cuad_actual, particion, mejor_valor, mejor_particion)

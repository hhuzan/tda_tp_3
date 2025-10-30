import math


def suma_cuadrados(sumas):
    return sum(s * s for s in sumas)


def backtracking(i, valores, k, sumas, grupos, mejor_valor, mejor_particion):

    if i == len(valores):
        actual = suma_cuadrados(sumas)
        if actual < mejor_valor:
            return actual, [list(g) for g in grupos]
        return mejor_valor, mejor_particion

    if suma_cuadrados(sumas) >= mejor_valor:
        return mejor_valor, mejor_particion

    for g in range(k):
        grupos[g].append(i)
        sumas[g] += valores[i]

        mejor_valor, mejor_particion = backtracking(
            i + 1, valores, k, sumas, grupos, mejor_valor, mejor_particion
        )

        sumas[g] -= valores[i]
        grupos[g].pop()

    return mejor_valor, mejor_particion


def resolver(k, valores):
    sumas = [0] * k
    grupos = [[] for _ in range(k)]
    mejor_valor = math.inf
    mejor_particion = None

    mejor_valor, mejor_particion = backtracking(
        0, valores, k, sumas, grupos, mejor_valor, mejor_particion
    )

    return mejor_valor, mejor_particion

import pulp
from pulp import PULP_CBC_CMD


def prog_lineal(k, habilidades):
    n = len(habilidades)

    modelo = pulp.LpProblem("Tribu_del_Agua", pulp.LpMinimize)

    # Variables
    y = pulp.LpVariable.dicts("y", (range(k), range(n)), cat="Binary")
    s = pulp.LpVariable.dicts("s", range(k))
    zmax = pulp.LpVariable("Zmax")
    zmin = pulp.LpVariable("Zmin")

    # Restricciones

    # Asignacion de maestros
    for j in range(n):
        modelo += pulp.lpSum(y[i][j] for i in range(k)) == 1

    # Definicion de sumas, zmax y zmin
    for i in range(k):
        modelo += s[i] == pulp.lpSum(habilidades[j] * y[i][j]
                                     for j in range(n))
        modelo += s[i] <= zmax
        modelo += s[i] >= zmin

    modelo += zmax - zmin

    modelo.solve(PULP_CBC_CMD(msg=False))

    particion = [[] for _ in range(k)]
    for i in range(k):
        for j in range(n):
            if y[i][j].value() == 1:
                particion[i].append(j)

    valor_objetivo = (zmax.value() - zmin.value())

    return valor_objetivo, particion

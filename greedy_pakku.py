def greedy_pakku(k, habilidades):
    ordenadas = sorted([(v, i)
                       for i, v in enumerate(habilidades)], reverse=True)
    sumas = [0]*k
    particion = [[] for _ in range(k)]
    for valor, indice in ordenadas:
        j = min(range(k), key=lambda x: sumas[x])
        particion[j].append(indice)
        sumas[j] += valor
    return sum(s*s for s in sumas), particion

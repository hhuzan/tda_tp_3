def greedy_ffd(k, habilidades):
    ordenadas = sorted([(v, i) for i, v in enumerate(habilidades)], reverse=True)
    
    sumas = [0] * k
    particion = [[] for _ in range(k)]

    for valor, indice in ordenadas:
        mejor_g = None
        mejor_aumento = float('inf')

        for g in range(k):
            aumento = (sumas[g] + valor)**2 - (sumas[g]**2)
            if aumento < mejor_aumento:
                mejor_aumento = aumento
                mejor_g = g

        particion[mejor_g].append(indice)
        sumas[mejor_g] += valor

    return sum(s*s for s in sumas), particion
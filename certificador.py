def es_particion_valida(maestros, k, B, particion):
    if len(particion) != k:
        return False

    vistos = set()
    for grupo in particion:
        for m in grupo:
            if m in vistos:
                return False
            vistos.add(m)

    if len(vistos) != len(maestros):
        return False

    suma_total = 0
    for grupo in particion:
        suma_grupo = 0
        for maestro in grupo:
            suma_grupo += maestros[maestro]
        suma_total += suma_grupo**2

    if suma_total > B:
        return False

    return True

def leer_archivo(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        lineas = [line.strip() for line in f if line.strip()]
    k = int(lineas[1])
    elementos = []
    for linea in lineas[2:]:
        nombre, habilidad = linea.split(",")
        elementos.append((nombre.strip(), float(habilidad.strip())))
    return k, elementos

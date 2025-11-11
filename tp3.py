from backtracking import resolver


def leer_archivo(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        lineas = [line.strip() for line in f if line.strip()]
    k = int(lineas[1])
    elementos = []
    for linea in lineas[2:]:
        nombre, habilidad = linea.split(",")
        elementos.append((nombre.strip(), float(habilidad.strip())))
    return k, elementos


def main():
    k, elementos = leer_archivo("datos/5_2.txt")
    nombres, habilidades = zip(*elementos)

    menor_suma, particion = resolver(k, habilidades)

    print(f"Mejor suma = {menor_suma}")
    for i, grupo in enumerate(particion, 1):
        lista_nombres = [nombres[j] for j in grupo]
        print(f"Grupo {i}: {lista_nombres}")


if __name__ == "__main__":
    main()

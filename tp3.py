import sys
from backtracking import resolver
from prog_lineal import prog_lineal
from greedy_pakku import greedy_pakku
from aproximacion import greedy_ffd
from lectura_archivo import leer_archivo
import time


def procesar_archivo(nombre_archivo):
    k, elementos = leer_archivo(nombre_archivo)
    nombres, habilidades = zip(*elementos)

    inicio = time.time()
    menor_suma, particion = resolver(k, habilidades)
    print("Backtraking")
    print(f"tiempo: {time.time()-inicio} seg")
    print(f"Mejor suma = {menor_suma}")
    for i, grupo in enumerate(particion, 1):
        lista_nombres = [nombres[j] for j in grupo]
        print(f"Grupo {i}: {lista_nombres}")

    print()
    print()

    inicio = time.time()
    menor_suma, particion = greedy_pakku(k, habilidades)
    print("Greedy Pakku")
    print(f"tiempo: {time.time()-inicio} seg")
    print(f"Mejor suma = {menor_suma}")
    for i, grupo in enumerate(particion, 1):
        lista_nombres = [nombres[j] for j in grupo]
        print(f"Grupo {i}: {lista_nombres}")

    print()
    print()

    inicio = time.time()
    menor_suma, particion = greedy_ffd(k, habilidades)
    print("Greedy FFD")
    print(f"tiempo: {time.time()-inicio} seg")
    print(f"Mejor suma = {menor_suma}")
    for i, grupo in enumerate(particion, 1):
        lista_nombres = [nombres[j] for j in grupo]
        print(f"Grupo {i}: {lista_nombres}")

    print()
    print()

    inicio = time.time()
    menor_suma, particion, desbalance = prog_lineal(k, habilidades)
    print("Programación Lineal")
    print(f"tiempo: {time.time()-inicio} seg")
    print(f"Mejor suma = {menor_suma}")
    print(f"Desbalance = {desbalance}")
    for i, grupo in enumerate(particion, 1):
        lista_nombres = [nombres[j] for j in grupo]
        print(f"Grupo {i}: {lista_nombres}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Uso: python3 tp3.py <ruta/a/entrada.txt>")
        sys.exit(1)

    try:
        procesar_archivo(sys.argv[1])
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

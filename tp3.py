from backtracking import resolver
from greedy_pakku import greedy_pakku
from prog_lineal import prog_lineal
from lectura_archivo import leer_archivo
import time


def main():
    k, elementos = leer_archivo("datos/10_5.txt")
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
    menor_suma, particion, desbalance = prog_lineal(k, habilidades)
    print("Programación Lineal")
    print(f"tiempo: {time.time()-inicio} seg")
    print(f"Mejor suma = {menor_suma}")
    print(f"Desbalance = {desbalance}")
    for i, grupo in enumerate(particion, 1):
        lista_nombres = [nombres[j] for j in grupo]
        print(f"Grupo {i}: {lista_nombres}")


if __name__ == "__main__":
    main()

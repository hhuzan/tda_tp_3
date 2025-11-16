import re
from lectura_archivo import leer_archivo
from backtracking import resolver


def leer_resultados_esperados(path):
    resultados = {}
    with open(path, "r", encoding="utf-8") as f:
        contenido = f.read()

    bloques = [b.strip() for b in contenido.split("\n\n") if b.strip()]

    for bloque in bloques:
        nombre_match = re.search(r"^([^\n]+\.txt)", bloque)
        if not nombre_match:
            continue
        nombre = nombre_match.group(1).strip()

        coeficiente_match = re.search(r"Coeficiente:\s*(.+)", bloque)
        if coeficiente_match:
            coeficiente = [e.strip()
                           for e in coeficiente_match.group(1).split(",")]
        else:
            coeficiente = []

        resultados[nombre] = {
            "coeficiente": coeficiente
        }

    return resultados


def ejecutar_tests(resultados_esperados, carpeta, leer_archivo, resolver):
    for nombre_archivo, datos in resultados_esperados.items():
        archivo_path = f"{carpeta}/{nombre_archivo}"
        print(f"===== Test: {nombre_archivo} =====")
        try:
            k, elementos = leer_archivo(archivo_path)
            nombres, habilidades = zip(*elementos)

            menor_suma, particion = resolver(k, habilidades)
            esperado = datos["coeficiente"][0]

            if int(menor_suma) == int(esperado):
                print("✅ Óptimo correcto")
            else:
                print(
                    f"❌ Óptimo calculado erróneo (Esperado {esperado}, Obtenido {menor_suma})")

            print(f"Menor Suma: {menor_suma}")
        except Exception as e:
            print(f"Error al procesar {archivo_path}: {e}")
        print()


if __name__ == "__main__":

    resultados_esperados_catedra = leer_resultados_esperados(
        "datos/Resultados Esperados.txt")
    print(resultados_esperados_catedra)
    ejecutar_tests(resultados_esperados_catedra,
                   "datos", leer_archivo, resolver)

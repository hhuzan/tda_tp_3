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

        # Coeficiente
        coef_match = re.search(r"Coeficiente:\s*(\d+)", bloque)
        coef = int(coef_match.group(1)) if coef_match else None

        # Grupos
        grupos = []
        grupo_matches = re.findall(r"Grupo \d+:\s*(.+)", bloque)
        for g in grupo_matches:
            nombres = [n.strip() for n in g.split(",")]
            grupos.append(nombres)

        resultados[nombre] = {
            "coeficiente": coef,
            "grupos": grupos
        }

    return resultados


def ejecutar_tests(resultados_esperados, carpeta, leer_archivo, resolver):
    for nombre_archivo, datos in resultados_esperados.items():
        archivo_path = f"{carpeta}/{nombre_archivo}"
        print(f"===== Test: {nombre_archivo} =====")
        try:
            k, elementos = leer_archivo(archivo_path)
            nombres, habilidades = zip(*elementos)

            menor_suma, particion_indices = resolver(k, habilidades)

            # Traducimos los índices a nombres
            particion = []
            for grupo in particion_indices:
                particion.append([nombres[i] for i in grupo])

            esperado_coef = datos["coeficiente"]
            grupos_esperados = datos["grupos"]

            if int(menor_suma) == esperado_coef:
                print("✅ Óptimo correcto")
                suma_ok = True
            else:
                print(f"❌ Óptimo calculado erróneo (Esperado {esperado_coef}, Obtenido {menor_suma})")
                suma_ok = False

            print(f"Menor Suma: {menor_suma}")

            # Verificamos grupos
            for i, grupo_calculado in enumerate(particion):
                grupo_esp = grupos_esperados[i] if i < len(grupos_esperados) else []
                if set(grupo_calculado) == set(grupo_esp):
                    print(f"✅ Grupo {i+1} correcto: {grupo_calculado}")
                else:
                    if suma_ok:
                        print(f"⚠️ Grupo {i+1} diferente pero suma correcta (Esperado {grupo_esp}, Obtenido {grupo_calculado})")
                    else:
                        print(f"❌ Grupo {i+1} incorrecto (Esperado {grupo_esp}, Obtenido {grupo_calculado})")

        except Exception as e:
            print(f"Error al procesar {archivo_path}: {e}")
        print()


if __name__ == "__main__":

    resultados_esperados_catedra = leer_resultados_esperados(
       "datos/Resultados Esperados.txt")
    
    resultados_esperados_alumnos = leer_resultados_esperados("datos_alumnos/resultados_esperados_alumnos.txt")

    ejecutar_tests(resultados_esperados_alumnos,
                   "datos_alumnos", leer_archivo, resolver)
    ejecutar_tests(resultados_esperados_catedra,
                   "datos", leer_archivo, resolver)

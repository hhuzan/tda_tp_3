import unittest

from certificador import es_particion_valida


class TestCertificador(unittest.TestCase):
    """Tests para verificar el correcto funcionamiento del certificador del Problema de la Tribu del Agua."""

    def test_particion_valida_basica(self):
        """Partición válida simple."""
        maestros = {0: 5, 1: 3, 2: 2}
        k, B = 2, 50
        particion = [[0], [1, 2]]  # (5)^2 + (3+2)^2 = 25 + 25 = 50
        self.assertTrue(es_particion_valida(maestros, k, B, particion))

    def test_particion_excede_B(self):
        """Cuando la suma de cuadrados excede B."""
        maestros = {0: 5, 1: 3, 2: 2}
        k, B = 2, 40
        particion = [[0], [1, 2]]  # 25 + 25 = 50 > 40
        self.assertFalse(es_particion_valida(maestros, k, B, particion))

    def test_cantidad_grupos_incorrecta(self):
        """Cantidad de grupos distinta de k."""
        maestros = {0: 5, 1: 3, 2: 2}
        k, B = 2, 100
        particion = [[0, 1, 2]]  # Solo 1 grupo, pero k=2
        self.assertFalse(es_particion_valida(maestros, k, B, particion))

    def test_elemento_repetido(self):
        """Un elemento aparece en más de un grupo."""
        maestros = {0: 5, 1: 3, 2: 2}
        k, B = 2, 100
        particion = [[0, 1], [1, 2]]  # Elemento 1 repetido
        self.assertFalse(es_particion_valida(maestros, k, B, particion))

    def test_elemento_faltante(self):
        """Falta algún elemento."""
        maestros = {0: 5, 1: 3, 2: 2}
        k, B = 2, 100
        particion = [[0], [1]]  # Falta el 2
        self.assertFalse(es_particion_valida(maestros, k, B, particion))

    def test_todos_en_un_grupo(self):
        """Todos los elementos en un solo grupo."""
        maestros = {0: 2, 1: 3, 2: 5}
        k, B = 1, 100
        particion = [[0, 1, 2]]  # (2+3+5)^2 = 100
        self.assertTrue(es_particion_valida(maestros, k, B, particion))

    def test_cada_en_grupo_separado(self):
        """Cada elemento en su propio grupo."""
        maestros = {0: 2, 1: 3, 2: 5}
        k, B = 3, 50
        particion = [[0], [1], [2]]  # 2² + 3² + 5² = 38
        self.assertTrue(es_particion_valida(maestros, k, B, particion))

    def test_particion_balanceada_valida(self):
        """Partición balanceada que cumple con B."""
        maestros = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6}
        k, B = 3, 150
        particion = [[0, 5], [1, 4], [2, 3]]  # 147 ≤ 150
        self.assertTrue(es_particion_valida(maestros, k, B, particion))

    def test_grupos_vacios_permitidos(self):
        """Grupos vacíos válidos si todos los elementos están asignados."""
        maestros = {0: 5, 1: 3}
        k, B = 3, 100
        particion = [[0], [1], []]  # Grupo vacío permitido
        self.assertTrue(es_particion_valida(maestros, k, B, particion))

    def test_caso_limite_B_justo(self):
        """Suma de cuadrados exactamente igual a B."""
        maestros = {0: 3, 1: 4}
        k, B = 2, 25
        particion = [[0], [1]]  # 9 + 16 = 25
        self.assertTrue(es_particion_valida(maestros, k, B, particion))

    def test_particion_vacia(self):
        """Caso extremo: sin maestros."""
        maestros = {}
        k, B = 1, 0
        particion = [[]]
        self.assertTrue(es_particion_valida(maestros, k, B, particion))

    def test_grupo_vacio_con_elementos_faltantes(self):
        """Grupos vacíos pero faltan elementos -> inválido."""
        maestros = {0: 5, 1: 3, 2: 2}
        k, B = 3, 100
        particion = [[0], [], []]  # Faltan 1 y 2
        self.assertFalse(es_particion_valida(maestros, k, B, particion))


if __name__ == "__main__":
    unittest.main()

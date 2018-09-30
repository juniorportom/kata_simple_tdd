from unittest import TestCase
from numbers import Numbers


class NumbersTest(TestCase):
    def test_calcular(self):
        self.assertEqual(Numbers().calcular(''), [], "Cadena vacia")

    def test_calcular_numeroElementos(self):
        self.assertEqual(Numbers().calcular('2')[0], 1, "Un elemento")
        self.assertEqual(Numbers().calcular('2,5'), [2], "Dos elementos")
        self.assertEqual(Numbers().calcular('2,5,7,8'), [4], "Varios elementos")

    def test_calcular_numeroElementos_minimo(self):
        self.assertEqual(Numbers().calcular('2,5,7,8'), [4, 2], "Varios elementos y el minimo")
        self.assertEqual(Numbers().calcular('4,5,7,8,1,9'), [6, 1], "Varios elementos y el minimo")

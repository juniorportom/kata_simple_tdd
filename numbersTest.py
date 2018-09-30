from unittest import TestCase
from numbers import Numbers


class NumbersTest(TestCase):
    def test_calcular(self):
        self.assertEqual(Numbers().calcular(''), [], "Cadena vacia")

    def test_calcular_numeroElementos(self):
        self.assertEqual(Numbers().calcular('2')[0], 1, "Un elemento")
        self.assertEqual(Numbers().calcular('2,5'), [2], "Dos elementos")
        self.assertEqual(Numbers().calcular('2,5,7,8'), [4], "Varios elementos")

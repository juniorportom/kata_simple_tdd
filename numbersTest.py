from unittest import TestCase
from numbers import Numbers


class NumbersTest(TestCase):
    def test_calcular(self):
        self.assertEqual(Numbers().calcular(''), [], "Cadena vacia")

    def test_calcular_numeroElementos(self):
        self.assertEqual(Numbers().calcular('2')[0], 1, "Un elemento")

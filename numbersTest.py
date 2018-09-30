from unittest import TestCase
from numbers import Numbers


class NumbersTest(TestCase):
    def test_calcular(self):
        self.assertEqual(Numbers().calcular(''), [], "Cadena vacia")

    def test_calcular_numeroElementos(self):
        self.assertEqual(Numbers().calcular('2')[0], 1, "Un elemento")
        self.assertEqual(Numbers().calcular('2,5')[0], 2, "Dos elementos")
        self.assertEqual(Numbers().calcular('2,5,7,8')[0], 4, "Varios elementos")

    def test_calcular_numeroElementos_minimo(self):
        self.assertEqual(Numbers().calcular('2,5,7,8')[:2], [4, 2], "Varios elementos y el minimo")
        self.assertEqual(Numbers().calcular('4,5,7,8,1,9')[:2], [6, 1], "Varios elementos y el minimo")

    def test_calcular_numeroElementos_minimo_maximo(self):
        self.assertEqual(Numbers().calcular('2,5,7,8')[:3], [4, 2, 8], "Varios elementos, el minimo y el maximo")
        self.assertEqual(Numbers().calcular('4,5,7,8,1,9')[:3], [6, 1, 9], "Varios elementos, el minimo y el maximo")

    def test_calcular_numeroElementos_minimo_maximo_promedio(self):
        self.assertEqual(Numbers().calcular('2,5,7,8'), [4, 2, 8, 5.5], "Varios elementos, el minimo y el maximo")
        self.assertEqual(Numbers().calcular('4,6,7,8,2,9'), [6, 2, 9, 6.0], "Varios elementos, el minimo y el maximo")



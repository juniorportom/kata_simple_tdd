from unittest import TestCase
from numbers import Numbers


class NumbersTest(TestCase):
    def test_calcular(self):
        self.assertEqual(Numbers().calcular(''), [], "Cadena vacia")

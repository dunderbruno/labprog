import unittest

from labtools import fatorial
from labtools import maximo
from labtools import minimo


class TestFatorial(unittest.TestCase):
    def test_int(self):
        """
        Testa a saída para a entrada de um número inteiro
        """
        result = fatorial(5)
        self.assertEqual(result, 120)


class TestMaximo(unittest.TestCase):
    def test_int_list(self):
        """
        Testa a saída para a entrada de uma lista de inteiros
        """
        lista = [1, 2, 3]
        result = maximo(lista)
        self.assertEqual(result, 3)


class TestMinimo(unittest.TestCase):
    def test_int_list(self):
        """
        Testa a saída para a entrada de uma lista de inteiros
        """
        lista = [1, 2, 3]
        result = minimo(lista)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
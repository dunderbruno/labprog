import unittest

from labtools import fatorial


class TestFatorial(unittest.TestCase):
    def test_int(self):
        """
        Testa a saída para a entrada de um número inteiro
        """
        result = fatorial(5)
        self.assertEqual(result, 120)


if __name__ == '__main__':
    unittest.main()
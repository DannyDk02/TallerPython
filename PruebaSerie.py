import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        numero = 5
        cadena = ''+str(numero)
        for i in range(numero-1):
            cadena = cadena + str(numero)

        self.assertEqual(cadena,'55555')


if __name__ == '__main__':
    unittest.main()

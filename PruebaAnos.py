import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        Años = 20
        Fecha = 2020
        Futuro = Años + (2070 - Fecha)

        self.assertEqual(Futuro, 70)

if __name__ == '__main__':
    unittest.main()

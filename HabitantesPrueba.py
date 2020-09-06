import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        poblacionA = 35
        poblacionB = 19.9
        tasaA = 0.02
        tasaB = 0.03

        while poblacionA > poblacionB:
            poblacionA = poblacionA + (poblacionA * 0.02)
            poblacionB = poblacionB + (poblacionB * 0.03)

        self.assertTrue(poblacionB>poblacionA)


if __name__ == '__main__':
    unittest.main()

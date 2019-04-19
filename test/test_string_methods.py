import unittest
from custom_functions.temperature_methods import promedio

class TestCollectionsMethods(unittest.TestCase):

    def test_promedio1(self):
        mes=(25,30,36,12,15,30,31,26,35,24,25,20)

        resultado=promedio(mes)
        self.assertAlmostEqual(resultado,25.75)

    def test_promedio2(self):
        uwi=(25,26,27)
        resultado=promedio(uwi)
        self.assertAlmostEqual(resultado,26)

    def test_promedio3(self):
        promedion=(60,42,50)
        resultado=promedio(promedion)
        self.assertAlmostEqual(resultado,50.666666666666664)

if __name__ == '__main__':
    unittest.main()


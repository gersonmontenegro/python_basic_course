import unittest

# this goes first
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    def test_es_mayor_de_edad(self):
        edad = 20
        res = es_mayor_de_edad(edad)
        self.assertEqual(res, True)
    def test_no_es_mayor_de_edad(self):
        edad = 17
        res = es_mayor_de_edad(edad)
        self.assertEqual(res, False)

if __name__ == '__main__':
    unittest.main()
import unittest
from clase7.funciones import suma, saludo

## ver TDD
class TestExamples(unittest.TestCase):
    
    def test_suma(self):
        print("test_suma iniciando... ")
        self.assertEqual(suma(2,2), 4)
        self.assertEqual(suma(1,2), 3)
        self.assertEqual(suma(1,1), 2)
            
    def test_saludo(self):
        print("test_saludo iniciando... ")
        self.assertEqual(saludo("Gus"), "hola Gus")
        with self.assertRaises(TypeError):
            saludo()
    
    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("foo".isupper())
        
    def test_split(self):
        s = "hello world"
        self.assertAlmostEqual(s.split(), ["hello", "world"])
        with self.assertRaises(TypeError):
            s.split(2)
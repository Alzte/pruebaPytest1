import  unittest
def suma(a, b):
    return a+b

def multiplicacion(a, b):
    return a*b

class Test(unittest.TestCase):
    def test_caso1(self):
        self.assertEqual(4, suma(2, 2))
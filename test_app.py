import unittest

def soma(a, b):
    return a + b

def saudacao(nome):
    return f"Olá, {nome}!"

def inverter_texto(texto):
    return texto[::-1]

class TestProjetoDevops(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativa(self):
        self.assertEqual(soma(-1, -1), -2)

    def test_saudacao(self):
        self.assertEqual(saudacao("Camilly"), "Olá, Camilly!")

    def test_inverter(self):
        self.assertEqual(inverter_texto("DevOps"), "spOveD")

    def test_texto_diferente(self):
        self.assertNotEqual(inverter_texto("Docker"), "Docker")

if __name__ == '__main__':
    unittest.main()
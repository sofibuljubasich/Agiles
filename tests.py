from main import Ahorcado
import unittest
juego = Ahorcado() #Ver de usar un init_test 

class TestAhorcado(unittest.TestCase):

    def test_arriesgar_palabra_correcta(self):
        self.assertTrue(juego.arriesgar_palabra("hola"))
    
    def test_arriesgar_palabra_incorrecta(self):
        self.assertFalse(juego.arriesgar_palabra("chau"))

    def test_arriesgar_letra_correcta(self):
        self.assertTrue(juego.arriesgar_letra("l"))
    
    def test_arriesgar_letra_incorrecta(self):
         self.assertFalse(juego.arriesgar_letra("k"))
    
    def test_devolver_posicion_letra_correcta(self):
        self.assertGreaterEqual(juego.devolver_posicion_letra("o"),0)
    
    def test_letra_correcta_no_pierde_intento(self):  
        juego.arriesgar_letra("l")
        self.assertEqual(juego.vidas,5)
    
    def test_letra_incorrecta_pierde_primer_intento(self):
        juego.arriesgar_letra("m")
        self.assertNotEqual(juego.vidas,6)

    def mostrar_letras_incorrectas(self):
        self.assertEquals(juego.letras_incorrectas,["k","m"])

    def muestra_letras_correctas_en_palabra(self):

        self.assertEqual(juego.palabraAhocardo,["_","_","l","_"])

if __name__ == '__main__':
   unittest.main()

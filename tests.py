from main import Ahorcado
import unittest

class TestAhorcado(unittest.TestCase):

    def test_arriesgar_palabra_correcta(self):
        juego = Ahorcado() 
        juego.palabraAdivinar="hola"
        self.assertTrue(juego.arriesgar_palabra("hola"))
    
    def test_arriesgar_palabra_incorrecta(self):
        juego = Ahorcado() 
        juego.palabraAdivinar="hola"
        self.assertFalse(juego.arriesgar_palabra("chau"))

    def test_arriesgar_letra_correcta(self):
        juego = Ahorcado() 
        juego.palabraAdivinar="hola"
        self.assertTrue(juego.arriesgar_letra("l"))
    
    def test_arriesgar_letra_incorrecta(self):
        juego = Ahorcado() 
        juego.palabraAdivinar="hola"
        self.assertFalse(juego.arriesgar_letra("k"))
    
    def test_devolver_posicion_letra_correcta(self):
        juego = Ahorcado() 
        juego.palabraAdivinar="hola"
        self.assertGreaterEqual(juego.devolver_posicion_letra("o"),0)
    
    def test_letra_correcta_no_pierde_intento(self):
        # revisar test  
        juego = Ahorcado() 
        juego.vidas = 6
        juego.palabraAdivinar= "hola"
        juego.palabraAhocardo = ["_","o","_","_"]
        self.assertEqual(juego.vidas,6)
    
    def test_letra_incorrecta_pierde_primer_intento(self):
        # revisar test
        juego = Ahorcado() 
        juego.palabraAdivinar= "hola"
        juego.vidas=6
        juego.arriesgar_letra("m")
        self.assertEqual(juego.vidas,5)

    def test_mostrar_letras_incorrectas(self):
        juego = Ahorcado() 
        juego.palabraAdivinar= "hola"
        juego.letras_incorrectas = ["k","m"]
    
        self.assertEqual(juego.mostrar_letras_incorrectas(),["k","m"])

    def test_muestra_letras_correctas_en_palabra(self):
        # revisar test
        juego = Ahorcado() 
        juego.palabraAdivinar= "hola"
        juego.palabraAhocardo = ["_","_","l","_"]
        self.assertEqual(juego.palabraAhocardo,["_","_","l","_"])
    
    def test_letra_incorrecta_repetida(self):
        juego = Ahorcado()

        juego.palabraAdivinar= "hola"
        juego.letras_incorrectas = ["x"]
        
        self.assertTrue(juego.chequear_letra_repetida("x"))

    def test_letra_correcta_repetida(self):
        juego = Ahorcado()
        juego.palabraAdivinar= "hola"
        juego.palabraAhocardo = ["_","_","_","a"]

        self.assertTrue(juego.chequear_letra_repetida("a"))

    
if __name__ == '__main__':
   unittest.main()

from main import Ahorcado
from main import LP as palabras
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
        juego.iniciar()

        juego.palabraAdivinar="hola"
        self.assertTrue(juego.arriesgar_letra("l"))
    
    def test_arriesgar_letra_incorrecta(self):
        juego = Ahorcado() 
        juego.palabraAdivinar="hola"
        self.assertFalse(juego.arriesgar_letra("k"))
    

    #Me parece que no es necesaario
    """def test_devolver_posicion_letra_correcta(self):
        juego = Ahorcado() 
        juego.palabraAdivinar="hola"
        self.assertGreaterEqual(juego.devolver_posicion_letra("o"),0)
    """
    def test_letra_correcta_no_pierde_intento(self):
        # revisar test el martes 17
        juego = Ahorcado() 
        juego.vidas = 6
        juego.palabraAdivinar= "hola"
        juego.palabraAhocardo = ["_","o","_","_"]
        juego.arriesgar("o")
        self.assertEqual(juego.vidas,6)
    
    def test_letra_incorrecta_pierde_primer_intento(self):
        # revisar test
        juego = Ahorcado() 
        juego.palabraAdivinar= "hola"
        juego.vidas=6
        juego.arriesgar("m")
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
        
        self.assertTrue(juego.pertenece_incorrectas("x"))

    def test_letra_correcta_repetida(self):
        juego = Ahorcado()
        juego.palabraAdivinar= "hola"
        juego.palabraAhocardo = ["_","_","_","a"]
       
        self.assertTrue(juego.pertenece_palabra("a"))

    def test_ignora_mayusculas_palabra(self):
        juego = Ahorcado()
        
        resultado = juego.formatear_input("mAYuS")
        self.assertEqual(resultado,"mayus")


    def test_ignora_mayuscula_letra(self):
        juego = Ahorcado()
        
        resultado = juego.formatear_input("A")
        self.assertEqual(resultado,"a")

    def test_letra_incorrecta_repetida_no_pierde(self):
        juego = Ahorcado()
        juego.iniciar()
        juego.palabraAdivinar = "programador"
        juego.palabraAhocardo = juego.inicializar_espacios("programador")
        juego.letras_incorrectas.append("i")
        juego.arriesgar("i")

        self.assertEqual(juego.vidas,6)

    def test_descuenta_vida(self):
        juego = Ahorcado()
        juego.iniciar()

        juego.arriesgar("ñ")

        self.assertEqual(juego.vidas,5)
    
    def test_pierde(self):

        juego = Ahorcado()
        juego.palabraAdivinar = "lunes"
        juego.vidas = 1
        juego.arriesgar("p")
        
        self.assertTrue(juego.perdio())
    
    def test_gana_x_letra(self):
        juego = Ahorcado()
        juego.palabraAdivinar = "ganador"
        juego.palabraAhocardo = ["g","a","n","a","_","o","r"]
        juego.arriesgar("d")
        self.assertTrue(juego.gano())

    def test_gana_x_palabra(self):
        juego = Ahorcado()
        juego.palabraAdivinar = "puerta"
        juego.palabraAhocardo = ["p","_","e","r","t","a"]
        juego.arriesgar("puerta")
        self.assertTrue(juego.gano())

    def test_inicializar_espacio(self):
        juego = Ahorcado()
        
        palabra = "hola"

        self.assertEqual(juego.inicializar_espacios(palabra),["_","_","_","_"])
    
    def test_genera_palabra_random(self):
        juego = Ahorcado()
      
        self.assertIn(juego.palabra_random(), palabras)

    def test_get_palabra(self):
        juego = Ahorcado()
        self.assertIsNotNone(juego.get_palabra())
    
    def test_es_letra(self):
        juego = Ahorcado()
        self.assertTrue(juego.es_letra("a"))
    
    
    def test_no_es_letra(self):
        juego = Ahorcado()
        self.assertFalse(juego.es_letra("hola"))

    




if __name__ == '__main__':
   unittest.main()

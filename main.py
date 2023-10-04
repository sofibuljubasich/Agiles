class Ahorcado:
    def __init__(self):
        self.palabraAdivinar = "hola"
        self.vidas = 6
        self.letras_incorrectas = []
        self.palabraAhocardo = ["_","_","_","_"]
        

    def get_palabra(self):
        return self.palabraAdivinar
        
    def arriesgar_palabra(self,palabra):
        return palabra == self.palabraAdivinar
    
    def arriesgar_letra(self,letra):
        if not self.chequear_letra_repetida(letra):
            if (letra in self.palabraAdivinar):
                posicion = self.devolver_posicion_letra(letra)
                self.palabraAhocardo[posicion]=letra
                print(self.palabraAhocardo)
                return True
            else:
                self.descontar_vida()
                self.letras_incorrectas.append(letra)
                return False
    
    def chequear_letra_repetida(self,letra):
        if ((letra in self.letras_incorrectas) or (letra in self.palabraAhocardo)):
            return True
        else:            
            return False
        
    def devolver_posicion_letra(self,letra):
        return self.palabraAdivinar.find(letra)
    
    def descontar_vida(self):
        self.vidas-=1

    def mostrar_letras_incorrectas(self):
        return self.letras_incorrectas
    
import random
LP = ["python", "flask", "hangman", "web", "programming"]

class Ahorcado:
    def __init__(self):
      
        self.vidas = 6
        self.letras_incorrectas = []
        self.palabraAdivinar = "" 
        self.palabraAhocardo = []
        
    def iniciar(self):
        self.palabraAdivinar = random.choice(LP)
        self.palabraAhocardo = ["_" for _ in self.palabraAdivinar] #PREGUNTAR SI DEBERIAMOS SEPARARLO
        self.vidas = 6
        self.letras_incorrectas = []

    def get_palabra(self):
        return self.palabraAdivinar
        
    def arriesgar_palabra(self,palabra):
        
        if (palabra == self.palabraAdivinar):
            self.palabraAhocardo = [i for a,i in enumerate(self.palabraAdivinar) ]
            return True
        else:
            self.descontar_vida()
            return False
    
   #REVISAR
    def arriesgar_letra(self,letra):
        if self.pertenece_palabra(letra):
            self.reemplazar_letra(letra)
            return True
        elif self.pertenece_incorrectas(letra):
            return True
        else:
            self.descontar_vida()
            self.letras_incorrectas.append(letra)
            return False
    """   def arriesgar_letra(self,letra):
        if not self.chequear_letra_repetida(letra):
            if (letra in self.palabraAdivinar):
                self.reemplazar_letra(letra)
                return True
            else:
                self.descontar_vida()
                self.letras_incorrectas.append(letra)
                return False
    """
    
    def reemplazar_letra(self,input):
        for idx, letra in enumerate(self.palabraAdivinar):
            if input == letra:
                self.palabraAhocardo[idx]=input
          
    def arriesgar(self,input):
        if len(input) == 1:
            return self.arriesgar_letra(input)
        else:
            print(input)
            return self.arriesgar_palabra(input)
    
    def pertenece_incorrectas(self,letra):
        return letra in self.letras_incorrectas
    
    
    def pertenece_palabra(self,letra):
        return letra in self.palabraAdivinar

    #Ver    
    def devolver_posicion_letra(self,letra):
        return self.palabraAdivinar.find(letra)
    
    def descontar_vida(self):
        self.vidas-=1

    def mostrar_letras_incorrectas(self):
        return self.letras_incorrectas
    

    def gano(self):
        estado = ''.join(self.palabraAhocardo)
        return estado == self.palabraAdivinar
    
    def perdio(self):
        return (self.vidas <1)
    
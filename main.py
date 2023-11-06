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
        self.palabraAhocardo = ["_" for _ in self.palabraAdivinar]
        self.vidas = 6
        self.letras_incorrectas = []

    def get_palabra(self):
        return self.palabraAdivinar
        
    def arriesgar_palabra(self,palabra):
        
        
        return palabra == self.palabraAdivinar
    
   
    def arriesgar_letra(self,letra):
        if not self.chequear_letra_repetida(letra):
            if (letra in self.palabraAdivinar):
                self.reemplazar_letra(letra)
                return True
            else:
                self.descontar_vida()
                self.letras_incorrectas.append(letra)
                return False
    
    def reemplazar_letra(self,input):
        for idx, letra in enumerate(self.palabraAdivinar):
            if input == letra:
                self.palabraAhocardo[idx]=input
          
    def arriesgar(self,input):
        print("ingresa",input)
        if len(input) == 1:
            print("letra")
            return self.arriesgar_letra(input)
        else:
            print("palarb")
            return self.arriesgar_palabra(input)
    
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
    
    def mostrar_palabra():
        pass

    def gano(self):
        estado = ''.join(self.palabraAhocardo)
        print(estado)
        return estado == self.palabraAdivinar
    
    def perdio(self):
        return (self.vidas <1)
    
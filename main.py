import random
LP = ["python", "flask", "hangman", "web", "programming"]

class Ahorcado:
    def __init__(self):
      
        self.vidas = 6
        self.letras_incorrectas = []
        self.palabraAdivinar = "" 
        self.palabraAhocardo = []
        
    def iniciar(self):
        self.palabraAdivinar = self.palabra_random()
        self.palabraAhocardo = self.inicializar_espacios(self.palabraAdivinar)
        self.vidas = 6
        self.letras_incorrectas = []
    
    #def mostrar_palabra_ahorcado(self,palabra):
        #resultado = palabra[0].capitalize() + "_".join(letra.capitalize() if letra.isalpha() else letra for letra in palabra[1:])

        #return resultado
    
    def palabra_random(self):
        return random.choice(LP)

    def inicializar_espacios(self,palabraAdivinar):
        return ["_" for _ in palabraAdivinar]
    
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
  
    
    def reemplazar_letra(self,input):
        for idx, letra in enumerate(self.palabraAdivinar):
            if input == letra:
                self.palabraAhocardo[idx]=input
          
    def arriesgar(self,input_form):
        input = self.formatear_input(input_form)
        if self.es_letra(input):
            return self.arriesgar_letra(input)
        else:
            print(input)
            return self.arriesgar_palabra(input)
    
    def es_letra(self,input):
        return (len(input)==1)
    
    def pertenece_incorrectas(self,letra):
        return letra in self.letras_incorrectas
    
    
    def pertenece_palabra(self,letra):
        return letra in self.palabraAdivinar

    #Ver    
    """def devolver_posicion_letra(self,letra):
        return self.palabraAdivinar.find(letra)"""
    
    def descontar_vida(self):
        self.vidas-=1

    def mostrar_letras_incorrectas(self):
        return self.letras_incorrectas


    def gano(self):
        estado = ''.join(self.palabraAhocardo)
        return estado == self.palabraAdivinar
    
    def perdio(self):
        return (self.vidas <1)
    
    def formatear_input(self,input):
        return input.lower()
    
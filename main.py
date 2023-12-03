import random
LP = ["agiles", "lenguaje", "framework", "assert", "metodologia","feature","aceptance","incremental"]
#LP = ["python", "flask", "hangman", "web", "programming"]

class Ahorcado:
    def __init__(self):
      
        self.vidas = 6
        self.letras_incorrectas = []
        self.palabra_adivinar = "" 
        self.palabra_ahocardo = []
        
    def iniciar(self):
        self.palabra_adivinar = self.palabra_random()
        self.palabra_ahocardo = self.inicializar_espacios(self.palabra_adivinar)
        self.vidas = 6
        self.letras_incorrectas = []
    
    
    def palabra_random(self):
        return random.choice(LP)

    def inicializar_espacios(self,palabra_adivinar):
        return ["_" for _ in palabra_adivinar]
    
    def get_palabra(self):
        return self.palabra_adivinar
        
    def arriesgar_palabra(self,palabra):
        
        if (palabra == self.palabra_adivinar):
            self.palabra_ahocardo = [i for a,i in enumerate(self.palabra_adivinar) ]
            return True
        else:
            self.descontar_vida()
            return False
    

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
  
    
    def reemplazar_letra(self,input_user):
        for idx, letra in enumerate(self.palabra_adivinar):
            if input_user == letra:
                self.palabra_ahocardo[idx]=input_user
          
    def arriesgar(self,input_form):
        input_user = self.formatear_input(input_form)
        if self.es_letra(input_user):
            return self.arriesgar_letra(input_user)
        else:
            return self.arriesgar_palabra(input_user)
    
    def es_letra(self,input_user):
        return (len(input_user)==1)
    
    def pertenece_incorrectas(self,letra):
        return letra in self.letras_incorrectas
    
    
    def pertenece_palabra(self,letra):
        return letra in self.palabra_adivinar

   
    def descontar_vida(self):
        self.vidas-=1

    def mostrar_letras_incorrectas(self):
        return self.letras_incorrectas


    def gano(self):
        estado = ''.join(self.palabra_ahocardo)
        return estado == self.palabra_adivinar
    
    def perdio(self):
        return (self.vidas <1)
    
    def formatear_input(self,input_user):
        return input_user.lower()
    
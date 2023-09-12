class Ahorcado:
    def __init__(self):
        self.palabraAdivinar = "hola"
    
    def get_palabra(self):
        return self.palabraAdivinar
    
    def arriesgar_palabra(self,palabra):
        return palabra == self.palabraAdivinar
    
    def arriesgar_letra(self,letra):
        return (letra in self.palabraAdivinar)
    
    def devolver_posicion_letra(self,letra):
        #Se le suma 1 para que la posicion sea intituiva 
        # para el jugador
        return self.palabraAdivinar.find(letra)+1 
    
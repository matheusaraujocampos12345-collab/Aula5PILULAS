class Fila:
    def __init__(self):
        self.fila = []
        
    def enqueue(self,elemento):
        self.fila.append(elemento)
        print('Elemento inserido')
        
    def denqueue(self):
        if len(self.fila) > 0:
            return self.fila.pop(0)
        return None 
    
    def vazia(self):
        return len(self.fila) > 0 
class Pilha:
    def __init__(self):
        self.dados = []
        
    def push(self, elemento):
        self.dados.append(elemento)
        
    def pop(self):
        if len(self.dados) > 0:
            return self.dados.pop()
        return None
    def vazia(self):
        return len(self.dados) == 0
    
from pilha import Pilha
def validar_expressao(expressao):
    p = Pilha()
    for c in expressao:
        if c == '(':
            p.push(c)
        elif c == ')':
            if p.vazia():
                return False
            p.pop()
            
    return p.vazia()

exp1 = '(a+b) - (5-9)'
exp2 = '(a+b-(4*5))-(5-9'
print(validar_expressao(exp1))
print(validar_expressao(exp2))
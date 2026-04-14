carrinho = ['notebook', 'mouse', 'teclado']
for item in carrinho:
    print(item)
    
carrinho.append('headset')
carrinho.remove('mouse')
carrinho.insert(1, 'monitor')
carrinho[0] = 'macbook'

for item in carrinho:
    print(item)
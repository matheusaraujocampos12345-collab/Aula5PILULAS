estoque = {
    1 : {'nome': 'notebook', 'preco' : 3500, 'qtd' : 12},
    2 : {'nome': 'monitor', 'preco' : 500, 'qtd' : 12},
    3 : {'nome': 'mouse', 'preco' : 300, 'qtd' : 12}
}

for codigo,produto in estoque.items():
    print(f'{codigo} - {produto['nome']} R$ {produto['preco']}')
    
    codigo = 1 
    quantidade = 10 
    if codigo in estoque:
        estoque[codigo]['qtd'] += quantidade
    
    for codigo,produto in estoque.items():
        print(f'{codigo} - {produto['nome']} R${produto['preco']} Qtd {produto['qtd']}')
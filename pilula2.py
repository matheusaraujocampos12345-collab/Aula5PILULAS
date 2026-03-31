def simuladorCrescimento(populaçao, taxa, limite):
    anos = 0
    
    while populaçao < limite:
        populaçao = populaçao * (1+ taxa)
        anos += 1
    return anos
#main
p = float(input('Digite a populalação: '))
t = float(input('Digite a taxa: '))/100
l = float(input('Digite o limite: '))

print(f'Anos: {simuladorCrescimento(p, t, l)}')
meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
salarios = []
for i in range(12):
    salarios.append(float(input(f'Salario de {meses[i]}: ')))
    
    soma = 0 
    for salario in salarios:
        soma += salario
        
    sal13 = soma / (len(salarios))
    feria = sal13 * 1/3
def validarSenha(senha):
    if len(senha) < 8:
        return 'Senha inválida, tente novamente'
    
    temNumero = False
    temMaiuscula = False
    
    for c in senha:
        if c == ' ':
            return 'Senha inválida, não pode conter espaços.'
        if c >= '0' and c <= '9':
            temNumero = True
        if c >= 'A' and c <= 'Z':
            temMaiuscula = True
    if not temNumero:
        return 'Senha inválida, não contem número'
    
    if not temMaiuscula:
        return 'Senha inválida, não contem maiúscula'
    
    return 'Senha válida.'
        
        
#main
senha = input('Digite a senha: ')
print(validarSenha(senha))

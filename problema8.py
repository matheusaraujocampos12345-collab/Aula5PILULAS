from fila import Fila
requisicao = Fila()
requisicao.enqueue('get /usuarios')
requisicao.enqueue('get /login')
requisicao.enqueue('get /aluno')

while not requisicao.vazia():
    req = requisicao.denqueue()
    print(req)
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b


def exibir_mensagem(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação = {resultado}")

exibir_mensagem(10, 10, somar) # o resultado da operação 10 + 10 = 20
exibir_mensagem(10, 10, subtrair) # o resultado da operação 10 - 10 = 20
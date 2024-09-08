def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("Retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um boa dia!")  

def depositar(valor):   
    saldo = 500
saldo += valor    # erro, faltou a indentação

sacar(400)
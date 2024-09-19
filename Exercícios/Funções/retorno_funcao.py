def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1


    return antecessor, sucessor

# Toda função Python retorna None por padrão. Diferente de outras linguagens de programação, em Python uma função pode retornar mais de um valor.

def funcao_none():
    print("Olá, Mundo!")
#   return None

print(calcular_total([10, 20, 34])) # 64
print(retorna_antecessor_e_sucessor(10)) # (9, 11)
print(funcao_none()) # None


# while True:
    
#     numero = int(input("Informe um número: "))

# Utliza o break para parar alguma situação específica dentro do laço

#     if numero == 10:
#         break

#     print(numero)


# for numero in range(100):

#     if numero == 12:
#         break
    
#     print(numero, end=" ")


# Utliza o continue para pular alguma situação específica dentro do laço
for numero in range(100):
      
      if numero % 2 == 0: # exibe apenas o números impares
          continue
    
      print(numero, end=" ")
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
            print(letra, end="")

print() # adiciona uma quebra de linha            

print("-----------------------------------")

texto = ""
VOGAIS = "AEIOU"

for letra in texto:
      if letra.upper() in VOGAIS:
            print(letra, end="")

else:
    print() # adiciona uma quebra de linha
    print("Executa no final do laço")              

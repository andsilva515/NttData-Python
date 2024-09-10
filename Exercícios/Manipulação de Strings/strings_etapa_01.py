nome = "joão da silva"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = " Olá mundo!    "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "CSharp"

print("#### " + menu + " ####")
print(menu.center(14))
print(menu.center(20, "#"))
print("P-y-t-h-o-n")
print("-".join(menu))

# usando a interação com o for

for letra in menu:
    print(letra, end="-")

print()
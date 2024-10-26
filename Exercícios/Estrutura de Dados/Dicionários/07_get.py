contatos = {"joao@gmail.com": {"nome": "João", "telefone": "3333-2221"}}

# contatos["chave"] # keyError

resultado = contatos.get("chave") # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "joao@gmail.com", {}  
)   # {"joao@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)
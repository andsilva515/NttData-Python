contatos = {"joao@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultados = contatos.pop("joao@gmail.com") #{'nome': 'Joao', 'telefone': '3333-2221'}

resultado = contatos.pop("joao@gmail.com", {}) # {}
print(resultado)
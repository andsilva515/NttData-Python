contatos = {
    "joao@gmail.com": {"nome": "Joao", "telefone": "3333-2212"},
    "marcos@gmail.com": {"nome": "Marcos", "telefone": "3344-2256"},
    "matheus@gmail.com": {"nome": "Matheus", "telefone": "3355-2278"},
    "lucas@gmail.com": {"nome": "Lucas", "telefone": "3366-2290", "extra": {"a": 1}},
}

telefone = contatos["marcos@gmail.com"]["telefone"] # "3344-2256"
print(telefone)

extra = contatos["lucas@gmail.com"] ["extra"]
print(extra)


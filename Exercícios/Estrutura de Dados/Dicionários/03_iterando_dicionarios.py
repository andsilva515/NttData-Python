contatos = {
    "joao@gmail.com": {"nome": "Joao", "telefone": "3333-2212"},
    "marcos@gmail.com": {"nome": "Marcos", "telefone": "3344-2256"},
    "matheus@gmail.com": {"nome": "Matheus", "telefone": "3355-2278"},
    "lucas@gmail.com": {"nome": "Lucas", "telefone": "3366-2290", "extra": {"a": 1}},
}

for chave in contatos:
    print(chave, contatos[chave])
    
    print("=" * 100)    
    
    for chave, valor in contatos.items():
         print(chave, valor)
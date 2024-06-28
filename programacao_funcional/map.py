lista_1 = [1, 2, 3]
dobro = map(lambda i: i * 2, lista_1)
print(list(dobro))

lista_2 = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 26}
]
somente_nomes = map(lambda pessoa: pessoa['nome'], lista_2)
print(list(somente_nomes))

somente_idade = map(lambda pessoa: pessoa['idade'], lista_2)
print(sum(somente_idade))

frases = map(
    lambda pessoa: f'{pessoa["nome"]} tem {pessoa["idade"]} anos.', 
    lista_2)
print(list(frases))

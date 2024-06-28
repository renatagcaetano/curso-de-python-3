compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14},
)


def calcular_preco_total(compra):
    return compra['quantidade'] * compra['preco']


totais = tuple(
    map(calcular_preco_total, compras)
)

print(f'Preços totais: {list(totais)}')
print(f'Total geral: {sum(totais)}')

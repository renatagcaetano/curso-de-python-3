def dobro(x):
    return x * 2


def quadrado(x):
    return x ** 2


if __name__ == '__main__':
    d = dobro
    print(d(5))

    q = quadrado
    print(q(5))

    funcoes = [dobro, quadrado] * 5

    for funcao, numero in zip(funcoes, range(1, 11)):
        print(f'O {funcao.__name__} de {numero} é {funcao(numero)}')

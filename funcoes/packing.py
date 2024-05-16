def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma_2(1, 2))
    print(soma_3(1, 2, 3))
    print(soma_n(1, 2, 3, 4, 5, 6, 7))

    tupla_nums = (1, 2, 3)
    print(soma_3(*tupla_nums))

    lista_nums = [1, 2, 3]
    print(soma_3)

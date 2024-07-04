def mapear(funcao, lista):
    return (funcao(elemento) for elemento in lista)


if __name__ == '__main__':
    print(list(mapear(lambda i: i ** 2, [2, 3, 4])))

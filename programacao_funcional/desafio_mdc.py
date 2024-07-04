def mdc(numeros):
    def calcular(divisor):
        return divisor if sum(map(lambda x: x % divisor, numeros)) == 0 \
            else calcular(divisor - 1)
    return calcular(min(numeros))


if __name__ == '__main__':
    print(mdc([21, 7]))  # 7
    print(mdc([125, 40]))  # 5
    print(mdc([9, 564, 66, 3]))  # 3
    print(mdc([55, 22]))  # 11
    print(mdc([15, 150]))  # 15
    print(mdc([7, 9]))  # 1

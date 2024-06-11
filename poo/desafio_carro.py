class Carro:
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        maxima = self.velocidade_maxima
        nova = self.velocidade_atual + delta
        self.velocidade_atual = nova if nova <= maxima else maxima

        return self.velocidade_atual

    def frear(self, delta=5):
        minima = 0
        nova = self.velocidade_atual - delta
        self.velocidade_atual = nova if nova >= minima else minima

        return self.velocidade_atual


if __name__ == '__main__':
    carro1 = Carro(180)

    for _ in range(25):
        print(carro1.acelerar(8))

    for _ in range(10):
        print(carro1.frear(delta=20))

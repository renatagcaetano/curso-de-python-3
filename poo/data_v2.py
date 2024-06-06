class Data:
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


data1 = Data(6, 6, 2024)
print(data1)

data2 = Data(ano=2025)
data2.dia = 8
print(data2)

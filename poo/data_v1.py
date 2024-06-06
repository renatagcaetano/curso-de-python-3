class Data:
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


data1 = Data()
data1.dia = 6
data1.mes = 6
data1.ano = 2024
print(data1)

data2 = Data()
data2.dia = 8
data2.mes = 5
data2.ano = 2025
print(data2)

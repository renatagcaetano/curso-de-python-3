palavra = 'Paralelepípedo'

for letra in palavra:
    print(letra, end='')

print('Fim')

aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']

for aprovado in aprovados:
    print(aprovado)

for posicao, nome in enumerate(aprovados):
    print(posicao + 1, nome)

dias_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta',
               'Quinta', 'Sexta', 'Sábado', 'Domingo')

for dia in dias_semana:
    print(f'Hoje é {dia}.')

for letra in set('Isso é um set'):
    print(letra)

for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)

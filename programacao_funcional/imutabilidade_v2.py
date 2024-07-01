from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

setlocale(LC_ALL, 'pt_BR')


def mes_31_dias(mes):
    return mdays[mes] == 31


def get_nome_mes(mes):
    return month_name[mes]


def meses(todos_meses, nome_mes):
    return f'{todos_meses}\n- {nome_mes}'


print(reduce(meses, map(get_nome_mes, filter(mes_31_dias, range(1, 13))),
             'Meses com 31 dias:'))

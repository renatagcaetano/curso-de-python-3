from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

setlocale(LC_ALL, 'pt_BR')

meses_31 = filter(lambda mes: mdays[mes] == 31, range(1, 13))
meses_nomes = map(lambda mes: month_name[mes], meses_31)
meses = reduce(lambda meses, mes: f'{meses}\n- {mes}', meses_nomes,
               'Meses com 31 dias:')

print(meses)

print(
    reduce(
        lambda meses, mes: f'{meses}\n- {mes}',
        map(
            lambda mes: month_name[mes],
            filter(
                lambda mes: mdays[mes] == 31,
                range(1, 13)
            )
        ),
        'Meses com 31 dias:'
    )
)
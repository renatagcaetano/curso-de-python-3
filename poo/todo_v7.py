from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    # Sobrecarga do operador +=
    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._adicionar_tarefa(tarefa)
        return self

    def _adicionar_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _adicionar_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def adicionar(self, tarefa, vencimento=None, **kwargs):
        # self.tarefas.append(Tarefa(descricao, vencimento))
        funcao_escolhida = self._adicionar_tarefa \
            if isinstance(tarefa, Tarefa) \
            else self._adicionar_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluída)')
        elif self.vencimento:
            if datetime.now() >= self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')

        return f'{self.descricao} ' + ' '.join(status)


class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias
        self.dono = None

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(self.descricao, novo_vencimento,
                                       self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa


def main():
    casa = Projeto('Tarefas de casa')
    casa.adicionar('Passar a roupa', datetime.now())
    casa.adicionar('Lavar a louça')
    # casa.adicionar(TarefaRecorrente('Trocar lençol', datetime.now(), 7))
    casa += TarefaRecorrente('Trocar lençol', datetime.now(), 7)
    # casa.adicionar(casa.procurar('Trocar lençol').concluir())
    casa.procurar('Trocar lençol').concluir()
    print(casa)

    casa.procurar('Lavar a louça').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')
    print(casa)

    mercado = Projeto('Compras no mercado')
    mercado.adicionar('Frutas secas')
    mercado.adicionar('Carne')
    mercado.adicionar('Tomate',  datetime.now()
                      + timedelta(days=3, seconds=1))
    print(mercado)

    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()
    for tarefa in mercado:
        print(f'- {tarefa}')
    print(mercado)


if __name__ == '__main__':
    main()

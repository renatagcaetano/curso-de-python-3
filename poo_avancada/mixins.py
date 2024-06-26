class HtmlToStringMixin:
    def __str__(self):
        # Conversão para HTML
        html = super().__str__() \
            .replace('(', '<strong>()') \
            .replace(')', ')</strong>')
        return f'<span>{html}</span>'


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


class Animal:
    def __init__(self, nome, pet=True):
        self.nome = nome
        self.pet = pet

    def __str__(self):
        return self.nome + ' (pet)' if self.pet else ''


class PessoaHtml(HtmlToStringMixin, Pessoa):
    pass


class AnimalHtml(HtmlToStringMixin, Animal):
    pass


if __name__ == '__main__':
    pessoa1 = Pessoa('Maria Eduarda')
    print(pessoa1)

    pessoa2 = PessoaHtml('Roberto Carlos')
    print(pessoa2)

    toto = AnimalHtml('Totó')
    print(toto)

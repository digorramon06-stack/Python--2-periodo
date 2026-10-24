class Filme:

    def __init__(self, titulo, diretor, ano):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano

    def resumo(self):
        return f'{(self.titulo)}, {(self.ano)}, {(self.diretor)}'


filme1 = Filme('Gente grande','Dennis Dugan', 2010)
filme2 = Filme('Deadpool', 'Tim Miller', 2016)

print(filme1.resumo())
print(filme2.resumo())

nTitulo = input('Informe o Titulo do Filme Novo: ')
nDiretor = input('Informe o Diretor do Filme Novo: ')
nAno = input('Informe o Ano do Filme Novo: ')

nFilme = (nTitulo, nDiretor, nAno)

print(nFilme.resumo())


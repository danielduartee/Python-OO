class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def likes(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

    def __str__ (self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__ (self):
        return f'{self._nome} - {self.ano} - {self.duracao} min {self._likes} Likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__ (self):
        return f'{self._nome} - {self.ano} - {self.temporadas} - {self._likes} Likes'

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    def __getitem__(self, item):
        return self._programas
        
    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

    def tamanho(self):
        return len(self.programas)

forma = Filme('a forma da agua', 2018, 160)
euphoria = Serie('euphora', 2020, 2)
labirinto = Filme('o Labirinto do fauno', 2006, 120)
midnight = Serie('midnight gospel', 2019, 1 )

forma.dar_like()
labirinto.dar_like()
euphoria.dar_like()
euphoria.dar_like()
midnight.dar_like()



filmes_e_series = [forma, euphoria, midnight, labirinto]
feriado = Playlist('feriado', filmes_e_series)

print(f'Tamanho: {len(feriado.listagem)}')

for programa in feriado.listagem:
    print(programa)


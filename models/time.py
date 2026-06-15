from models.jogador import Jogador
from models.tecnico import Tecnico


class Time:

    def __init__(
        self,
        id: int,
        nome: str,
        tecnico: Tecnico
    ):
        self.__id = id
        self.__nome = nome
        self.__tecnico = tecnico

        self.__jogadores = []

        self.__pontuacao = 0

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def tecnico(self):
        return self.__tecnico

    @property
    def jogadores(self):
        return self.__jogadores

    @property
    def pontuacao(self):
        return self.__pontuacao

    def adicionar_jogador(self, jogador: Jogador):

        if len(self.__jogadores) >= 5:
            raise Exception("O time já possui 5 jogadores.")

        if jogador in self.__jogadores:
            raise Exception("Jogador já pertence ao time.")

        self.__jogadores.append(jogador)

    def remover_jogador(self, jogador: Jogador):
        if jogador not in self.__jogadores:
            raise Exception("Jogador não pertence ao time.")
        self.__jogadores.remove(jogador)

    def adicionar_pontos(self, pontos: int):
        self.__pontuacao += pontos

    def to_dict(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "tecnico": self.__tecnico.to_dict(),
            "jogadores": [
                jogador.to_dict()
                for jogador in self.__jogadores
            ],
            "pontuacao": self.__pontuacao
        }
    

    @staticmethod
    def from_dict(data):

        tecnico = Tecnico.from_dict(data["tecnico"])

        time = Time(
            data["id"],
            data["nome"],
            tecnico
        )

        for jogador_data in data["jogadores"]:
            jogador = Jogador.from_dict(jogador_data)
            time.adicionar_jogador(jogador)

        time.__pontuacao = data["pontuacao"]

        return time

    def __str__(self):
        jogadores = ", ".join(
        jogador.nickname
        for jogador in self.__jogadores )

        return (
            f"Time: {self.__nome}\n"
            f"Técnico: {self.__tecnico.nome}\n"
            f"Jogadores: {jogadores}\n"
            f"Pontos: {self.__pontuacao}"
        )
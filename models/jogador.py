from models.pessoa import Pessoa
from enums.funcao_jogador import FuncaoJogador


class Jogador(Pessoa):

    def __init__(
        self,
        id: int,
        nome: str,
        email: str,
        nickname: str,
        funcao: FuncaoJogador
    ):
        super().__init__(id, nome, email)

        self.__nickname = nickname
        self.__funcao = funcao

        self.__kills = 0
        self.__deaths = 0
        self.__assists = 0

    @property
    def nickname(self):
        return self.__nickname

    @property
    def funcao(self):
        return self.__funcao

    @property
    def kills(self):
        return self.__kills

    @property
    def deaths(self):
        return self.__deaths

    @property
    def assists(self):
        return self.__assists

    def adicionar_kill(self):
        self.__kills += 1

    def adicionar_death(self):
        self.__deaths += 1

    def adicionar_assist(self):
        self.__assists += 1

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "nickname": self.__nickname,
            "funcao": self.__funcao.value,
            "kills": self.__kills,
            "deaths": self.__deaths,
            "assists": self.__assists
        }
    

    @staticmethod
    def from_dict(data):
        jogador = Jogador(
            data["id"],
            data["nome"],
            data["email"],
            data["nickname"],
            FuncaoJogador(data["funcao"])
        )

        jogador.__kills = data["kills"]
        jogador.__deaths = data["deaths"]
        jogador.__assists = data["assists"]

        return jogador

    def __str__(self):
        return f"{self.nickname} - {self.funcao.value}"
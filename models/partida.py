from enums.status_partida import StatusPartida
from models.time import Time


class Partida:

    def __init__(
        self,
        id: int,
        time_a: Time,
        time_b: Time
    ):
        self.__id = id

        self.__time_a = time_a
        self.__time_b = time_b

        self.__placar_a = 0
        self.__placar_b = 0

        self.__status = StatusPartida.AGENDADA

        self.__vencedor = None

    @property
    def status(self):
        return self.__status

    @property
    def vencedor(self):
        return self.__vencedor

    def iniciar_partida(self):
        self.__status = StatusPartida.EM_ANDAMENTO

    def finalizar_partida(
        self,
        placar_a: int,
        placar_b: int
    ):

        self.__placar_a = placar_a
        self.__placar_b = placar_b

        self.__status = StatusPartida.FINALIZADA

        self.definir_vencedor()

    def definir_vencedor(self):

        if self.__placar_a > self.__placar_b:
            self.__vencedor = self.__time_a

        elif self.__placar_b > self.__placar_a:
            self.__vencedor = self.__time_b

    def to_dict(self):
        return {
            "id": self.__id,
            "time_a": self.__time_a.to_dict(),
            "time_b": self.__time_b.to_dict(),
            "placar_a": self.__placar_a,
            "placar_b": self.__placar_b,
            "status": self.__status.value,
            "vencedor": (
                self.__vencedor.nome
                if self.__vencedor
                else None
            )
        }
    
    @property
    def id(self):
        return self.__id

    @staticmethod
    def from_dict(data):

        time_a = Time.from_dict(data["time_a"])
        time_b = Time.from_dict(data["time_b"])

        partida = Partida(
            data["id"],
            time_a,
            time_b
        )

        partida.__placar_a = data["placar_a"]
        partida.__placar_b = data["placar_b"]

        partida.__status = StatusPartida(data["status"])

        partida.definir_vencedor()

        return partida

    def __str__(self):
        return f"{self.__time_a.nome} vs {self.__time_b.nome}"
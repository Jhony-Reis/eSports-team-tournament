from models.pessoa import Pessoa


class Tecnico(Pessoa):

    def __init__(
        self,
        id: int,
        nome: str,
        email: str,
        estrategia: str
    ):
        super().__init__(id, nome, email)

        self.__estrategia = estrategia

    @property
    def estrategia(self):
        return self.__estrategia

    @estrategia.setter
    def estrategia(self, estrategia: str):
        self.__estrategia = estrategia

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "estrategia": self.__estrategia
        }
    
    @property
    def id(self):
        return self._id

    @staticmethod
    def from_dict(data):
        return Tecnico(
            data["id"],
            data["nome"],
            data["email"],
            data["estrategia"]
        )

    def __str__(self):
        return f"Técnico: {self.nome}"
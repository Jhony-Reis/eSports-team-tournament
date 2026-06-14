from abc import ABC


class Pessoa(ABC):

    def __init__(self, id: int, nome: str, email: str):
        self._id = id
        self._nome = nome
        self._email = email

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @email.setter
    def email(self, email: str):
        self._email = email

    def to_dict(self):
        return {
            "id": self._id,
            "nome": self._nome,
            "email": self._email
        }

    def __str__(self):
        return f"{self._nome} ({self._email})"
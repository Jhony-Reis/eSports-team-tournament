from models.time import Time
from persistence.json_manager import JsonManager
from utils.config import TIMES_JSON


class TimeRepository:

    def listar(self):

        dados = JsonManager.ler(TIMES_JSON)

        return [
            Time.from_dict(item)
            for item in dados
        ]

    def salvar(self, time: Time):

        if self.buscar_por_id(time.id):

            raise ValueError(
                f"Já existe um time com ID {time.id}."
            )

        times = JsonManager.ler(TIMES_JSON)

        times.append(time.to_dict())

        JsonManager.escrever(
            TIMES_JSON,
            times
        )

    def buscar_por_id(self, id: int):

        times = self.listar()

        for time in times:

            if time.id == id:
                return time

        return None

    def atualizar(self, time_atualizado: Time):

        times = JsonManager.ler(TIMES_JSON)

        for i, time in enumerate(times):

            if time["id"] == time_atualizado.id:

                times[i] = time_atualizado.to_dict()

                break

        JsonManager.escrever(
            TIMES_JSON,
            times
        )

    def deletar(self, id: int):

        times = JsonManager.ler(TIMES_JSON)

        times = [
            time
            for time in times
            if time["id"] != id
        ]

        JsonManager.escrever(
            TIMES_JSON,
            times
        )
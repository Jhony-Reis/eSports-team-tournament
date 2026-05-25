from services.partida_service import (
    PartidaService
)

from repositories.time_repository import (
    TimeRepository
)

from models.partida import Partida


def menu_partida():

    service = PartidaService()

    time_repository = (
        TimeRepository()
    )

    while True:

        print("\n=== MENU PARTIDA ===")

        print("1 - Criar partida")
        print("2 - Listar partidas")
        print("3 - Finalizar partida")
        print("0 - Voltar")

        opcao = input("\nEscolha: ")

        match opcao:

            case "1":

                try:

                    id = int(input("ID: "))

                    time_a_id = int(
                        input("ID Time A: ")
                    )

                    time_b_id = int(
                        input("ID Time B: ")
                    )

                    time_a = (
                        time_repository
                        .buscar_por_id(
                            time_a_id
                        )
                    )

                    time_b = (
                        time_repository
                        .buscar_por_id(
                            time_b_id
                        )
                    )

                    if not time_a or not time_b:
                        print(
                            "\nTimes inválidos."
                        )
                        continue

                    partida = Partida(
                        id,
                        time_a,
                        time_b
                    )

                    service._PartidaService__repository.salvar(
                        partida
                    )

                    print("\nPartida criada.")

                except Exception as e:
                    print(f"\nErro: {e}")

            case "2":

                partidas = (
                    service.listar_partidas()
                )

                if not partidas:
                    print("\nNenhuma partida.")

                for partida in partidas:
                    print(partida)

            case "3":

                try:

                    partida_id = int(
                        input("ID da partida: ")
                    )

                    placar_a = int(
                        input("Placar Time A: ")
                    )

                    placar_b = int(
                        input("Placar Time B: ")
                    )

                    partida = (
                        service.buscar_partida(
                            partida_id
                        )
                    )

                    if not partida:
                        print(
                            "\nPartida não encontrada."
                        )
                        continue

                    service.finalizar_partida(
                        partida,
                        placar_a,
                        placar_b
                    )

                    print(
                        "\nPartida finalizada."
                    )

                except Exception as e:
                    print(f"\nErro: {e}")

            case "0":
                break

            case _:
                print("\nOpção inválida.")
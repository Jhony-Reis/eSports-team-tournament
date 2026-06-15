from services.time_service import (
    TimeService
)

from repositories.jogador_repository import (
    JogadorRepository
)

from models.time import Time
from models.tecnico import Tecnico


def menu_time():

    service = TimeService()

    jogador_repository = (
        JogadorRepository()
    )

    while True:

        print("\n=== MENU TIME ===")

        print("1 - Criar time")
        print("2 - Listar times")
        print("3 - Adicionar jogador")
        print("4 - Remover jogador")
        print("0 - Voltar")

        opcao = input("\nEscolha: ")

        match opcao:

            case "1":

                try:

                    id = int(input("ID: "))
                    nome = input("Nome do time: ")

                    print("\n=== Técnico ===")

                    tecnico_id = int(
                        input("ID técnico: ")
                    )

                    tecnico_nome = input(
                        "Nome técnico: "
                    )

                    tecnico_email = input(
                        "Email técnico: "
                    )

                    estrategia = input(
                        "Estratégia: "
                    )

                    tecnico = Tecnico(
                        tecnico_id,
                        tecnico_nome,
                        tecnico_email,
                        estrategia
                    )

                    time = Time(
                        id,
                        nome,
                        tecnico
                    )

                    service.criar_time(time)

                    print("\nTime criado.")

                except Exception as e:
                    print(f"\nErro: {e}")

            case "2":

                times = service.listar_times()

                if not times:
                    print("\nNenhum time.")

                for time in times:
                    print(time)
                    print("-" * 20)

            case "3":

                try:

                    time_id = int(
                        input("ID do time: ")
                    )

                    jogador_id = int(
                        input("ID do jogador: ")
                    )

                    time = service.buscar_time(
                        time_id
                    )

                    jogador = (
                        jogador_repository
                        .buscar_por_id(
                            jogador_id
                        )
                    )

                    if not time:
                        print(
                            "\nTime não encontrado."
                        )
                        continue

                    if not jogador:
                        print(
                            "\nJogador não encontrado."
                        )
                        continue

                    service.adicionar_jogador(
                        time,
                        jogador
                    )

                    print(
                        "\nJogador adicionado."
                    )

                except Exception as e:
                    print(f"\nErro: {e}")

            case "4":

                try:

                    time_id = int(
                        input("ID do time: ")
                    )

                    jogador_id = int(
                        input("ID do jogador: ")
                    )

                    time = service.buscar_time(
                        time_id
                    )

                    jogador = (
                        jogador_repository
                        .buscar_por_id(
                            jogador_id
                        )
                    )

                    if not time:
                        print(
                            "\nTime não encontrado."
                        )
                        continue

                    if not jogador:
                        print(
                            "\nJogador não encontrado."
                        )
                        continue

                    service.remover_jogador(
                        time,
                        jogador
                    )

                    print(
                        "\nJogador removido."
                    )

                except Exception as e:
                    print(f"\nErro: {e}")

            case "0":
                break

            case _:
                print("\nOpção inválida.")
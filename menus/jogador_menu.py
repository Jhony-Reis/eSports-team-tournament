from services.jogador_service import (
    JogadorService
)

from models.jogador import Jogador

from enums.funcao_jogador import (
    FuncaoJogador
)


def menu_jogador():

    service = JogadorService()

    while True:

        print("\n=== MENU JOGADOR ===")

        print("1 - Cadastrar jogador")
        print("2 - Listar jogadores")
        print("0 - Voltar")

        opcao = input("\nEscolha: ")

        match opcao:

            case "1":

                try:

                    id = int(input("ID: "))
                    nome = input("Nome: ")
                    email = input("Email: ")
                    nickname = input("Nickname: ")

                    print("\nFunções:")
                    print("ENTRY")
                    print("SUPPORT")
                    print("AWP")
                    print("IGL")
                    print("LURKER")

                    funcao = FuncaoJogador(
                        input("Função: ").upper()
                    )

                    jogador = Jogador(
                        id,
                        nome,
                        email,
                        nickname,
                        funcao
                    )

                    service.cadastrar_jogador(
                        jogador
                    )

                    print(
                        "\nJogador cadastrado."
                    )

                except Exception as e:
                    print(f"\nErro: {e}")

            case "2":

                jogadores = (
                    service.listar_jogadores()
                )

                if not jogadores:
                    print("\nNenhum jogador.")

                for jogador in jogadores:
                    print(jogador)

            case "0":
                break

            case _:
                print("\nOpção inválida.")
# Sistema de Torneio eSports

Projeto desenvolvido em Python utilizando **Programação Orientada a Objetos (POO)** para gerenciamento de torneios de eSports.

---

# Funcionalidades

O sistema permite:

- Cadastro de jogadores
- Criação de times
- Cadastro de técnicos
- Criação de torneios
- Geração automática de confrontos
- Registro de partidas
- Persistência de dados utilizando arquivos JSON
- Controle de ranking
- Gerenciamento de estatísticas dos jogadores

---

# Tecnologias Utilizadas

- Python 3
- Programação Orientada a Objetos (POO)
- JSON para persistência de dados
- Arquitetura em camadas

---

# Estrutura do Projeto

```text
esports_tournament/
│
├── data/
│   ├── jogadores.json
│   ├── times.json
│   ├── partidas.json
│   └── torneios.json
│
├── enums/
│   ├── funcao_jogador.py
│   ├── status_partida.py
│   └── tipo_torneio.py
│
├── menus/
│   ├── jogador_menu.py
│   ├── time_menu.py
│   ├── partida_menu.py
│   └── torneio_menu.py
│
├── models/
│   ├── pessoa.py
│   ├── jogador.py
│   ├── tecnico.py
│   ├── time.py
│   ├── partida.py
│   ├── torneio.py
│   ├── ranking.py
│   └── estatistica.py
│
├── persistence/
│   └── json_manager.py
│
├── repositories/
│   ├── jogador_repository.py
│   ├── time_repository.py
│   ├── partida_repository.py
│   └── torneio_repository.py
│
├── services/
│   ├── jogador_service.py
│   ├── time_service.py
│   ├── partida_service.py
│   ├── torneio_service.py
│   ├── ranking_service.py
│   └── estatistica_service.py
│
├── utils/
│   ├── config.py
│   ├── exceptions.py
│   └── validators.py
│
├── tests/
│
├── main.py
└── README.md
```

---

# Pré-requisitos

Antes de executar o projeto, certifique-se de possuir:

- Python 3.10 ou superior instalado

Verificar versão instalada:

```bash
python --version
```

ou

```bash
python3 --version
```

---

# Configuração Inicial

## 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
```

---

## 2. Entrar na pasta do projeto

```bash
cd esports_tournament
```

---

# Configuração da Pasta `data`

Criar os seguintes arquivos dentro da pasta `data/`:

```text
data/
 ├── jogadores.json
 ├── times.json
 ├── partidas.json
 └── torneios.json
```

Todos os arquivos devem iniciar contendo:

```json
[]
```

---

# Como Executar o Sistema

Na raiz do projeto, execute:

```bash
python main.py
```

ou

```bash
python3 main.py
```

---

# Fluxo Recomendado de Uso

## 1. Cadastrar jogadores

Menu:

```text
Jogadores -> Cadastrar jogador
```

---

## 2. Criar times

Menu:

```text
Times -> Criar time
```

---

## 3. Adicionar jogadores aos times

Menu:

```text
Times -> Adicionar jogador
```

---

## 4. Criar torneio

Menu:

```text
Torneios -> Criar torneio
```

---

## 5. Adicionar times ao torneio

Menu:

```text
Torneios -> Adicionar time
```

---

## 6. Gerar confrontos

Menu:

```text
Torneios -> Gerar confrontos
```

---

## 7. Finalizar partidas

Menu:

```text
Partidas -> Finalizar partida
```

---

# Conceitos de POO Utilizados

O projeto utiliza os seguintes conceitos:

- Encapsulamento
- Herança
- Abstração
- Composição
- Separação de responsabilidades
- Arquitetura em camadas

---

# Arquitetura do Sistema

Fluxo principal da aplicação:

```text
Menus
   ↓
Services
   ↓
Repositories
   ↓
JsonManager
   ↓
Arquivos JSON
```

---

# Persistência de Dados

Os dados do sistema são armazenados localmente utilizando arquivos JSON na pasta:

```text
data/
```

O sistema realiza automaticamente:

- Leitura
- Escrita
- Atualização
- Remoção de dados

---

# Tratamento de Erros

O sistema possui tratamento básico para:

- Emails inválidos
- Nicknames inválidos
- Time lotado
- Partidas já finalizadas
- IDs inexistentes
- Opções inválidas de menu

---

# Melhorias Futuras

Possíveis melhorias futuras para o projeto:

- Interface gráfica
- API REST
- Banco de dados SQL
- Sistema de login
- Geração automática de IDs
- Testes automatizados
- Docker
- Relatórios estatísticos

---

# Desenvolvedores

Projeto acadêmico desenvolvido para a disciplina de **Programação Orientada a Objetos**.

---

# Licença

Projeto desenvolvido apenas para fins educacionais.

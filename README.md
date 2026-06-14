# Sistema de Gerenciamento de Torneios eSports

## Descrição

O Sistema de Gerenciamento de Torneios eSports é uma aplicação desenvolvida em Python utilizando Programação Orientada a Objetos (POO). O objetivo do projeto é permitir o gerenciamento de jogadores, técnicos, times, partidas e torneios de eSports, aplicando conceitos fundamentais de engenharia de software e arquitetura em camadas.

Os dados são persistidos em arquivos JSON, dispensando a utilização de um banco de dados relacional e facilitando a execução do projeto em ambientes acadêmicos.

---

## Funcionalidades

* Cadastro de jogadores
* Cadastro de técnicos
* Criação de times
* Associação de jogadores aos times
* Criação de torneios
* Associação de times aos torneios
* Geração automática de confrontos
* Criação e finalização de partidas
* Controle de ranking
* Registro de estatísticas
* Persistência de dados utilizando arquivos JSON

---

## Tecnologias Utilizadas

* Python 3
* Programação Orientada a Objetos (POO)
* Arquivos JSON
* Arquitetura em Camadas

---

## Conceitos de POO Aplicados

### Encapsulamento

Os atributos das entidades são protegidos e acessados por meio de propriedades e métodos específicos.

### Herança

A classe `Pessoa` serve como classe base para:

* Jogador
* Técnico

### Abstração

A classe `Pessoa` é implementada como uma classe abstrata, definindo comportamentos comuns às subclasses.

### Composição

Um time é composto por:

* Técnico
* Lista de jogadores

Um torneio é composto por:

* Times
* Partidas

---

## Estrutura do Projeto

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

## Arquitetura do Sistema

O projeto segue uma arquitetura em camadas para promover separação de responsabilidades e facilitar a manutenção.

```text
Main
 ↓
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

### Camadas

#### Menus

Responsáveis pela interação com o usuário.

#### Services

Contêm as regras de negócio e validações.

#### Repositories

Responsáveis pelas operações de persistência dos dados.

#### JsonManager

Responsável pela leitura e escrita dos arquivos JSON.

---

## Pré-requisitos

Antes de executar o projeto, certifique-se de possuir:

* Python 3.10 ou superior

Verificar versão:

```bash
python --version
```

ou

```bash
python3 --version
```

---

## Configuração Inicial

### Clonar o Repositório

```bash
git clone <url-do-repositorio>
```

### Entrar na Pasta do Projeto

```bash
cd esports_tournament
```

---

## Configuração dos Arquivos de Dados

Criar os seguintes arquivos dentro da pasta `data`:

```text
jogadores.json
times.json
partidas.json
torneios.json
```

Todos devem iniciar com:

```json
[]
```

---

## Execução do Sistema

Na raiz do projeto execute:

```bash
python main.py
```

ou

```bash
python3 main.py
```

---

## Fluxo de Utilização

### 1. Cadastrar Jogadores

Menu:

```text
Jogadores → Cadastrar Jogador
```

### 2. Criar Times

Menu:

```text
Times → Criar Time
```

### 3. Adicionar Jogadores aos Times

Menu:

```text
Times → Adicionar Jogador
```

### 4. Criar Torneios

Menu:

```text
Torneios → Criar Torneio
```

### 5. Adicionar Times ao Torneio

Menu:

```text
Torneios → Adicionar Time
```

### 6. Gerar Confrontos

Menu:

```text
Torneios → Gerar Confrontos
```

### 7. Finalizar Partidas

Menu:

```text
Partidas → Finalizar Partida
```

---

## Regras de Negócio

### Jogadores

* Devem possuir ID único.
* Devem possuir email válido.
* Devem possuir nickname com pelo menos 3 caracteres.

### Times

* Devem possuir um técnico.
* Podem possuir no máximo 5 jogadores.

### Partidas

* Possuem dois times participantes.
* Possuem status:

  * AGENDADA
  * EM_ANDAMENTO
  * FINALIZADA
* Não podem ser reiniciadas após serem finalizadas.

### Torneios

* Podem ser:

  * PONTOS_CORRIDOS
  * ELIMINACAO_SIMPLES
* Podem possuir vários times e partidas.

### Ranking

* Vitória: 3 pontos
* Derrota: 0 pontos

---

## Persistência de Dados

Todos os dados são armazenados em arquivos JSON localizados na pasta:

```text
data/
```

A persistência é realizada automaticamente durante as operações de cadastro, atualização e remoção.

---

## Tratamento de Erros

O sistema trata situações como:

* Email inválido
* Nickname inválido
* Time lotado
* Partida já finalizada
* IDs inexistentes
* Opções inválidas de menu

---

## Possíveis Melhorias Futuras

* Interface gráfica
* API REST
* Banco de dados relacional
* Sistema de autenticação
* Geração automática de IDs
* Testes automatizados
* Containerização com Docker
* Relatórios estatísticos avançados

---

## Desenvolvedores

Projeto acadêmico desenvolvido para a disciplina de Programação Orientada a Objetos.

---

## Licença

Projeto desenvolvido exclusivamente para fins educacionais.

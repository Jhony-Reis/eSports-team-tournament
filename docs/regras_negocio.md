# Regras de Negócio

## 1. Cadastro de Jogadores

- Todo jogador deve possuir:
  - ID único
  - Nome
  - Email válido
  - Nickname
  - Função no time

- O email deve conter o caractere `@`.

- O nickname deve possuir no mínimo 3 caracteres.

- Cada jogador possui estatísticas individuais:
  - kills
  - deaths
  - assists

---

## 2. Funções dos Jogadores

As funções disponíveis são:

- ENTRY
- SUPPORT
- AWP
- IGL
- LURKER

Cada jogador deve possuir apenas uma função principal.

---

## 3. Cadastro de Técnicos

- Todo técnico deve possuir:
  - ID único
  - Nome
  - Email
  - Estratégia principal

---

## 4. Criação de Times

- Todo time deve possuir:
  - ID único
  - Nome
  - Técnico responsável

- Um time pode possuir no máximo:
  - 5 jogadores

- O sistema impede adicionar jogadores acima do limite permitido.

---

## 5. Partidas

- Toda partida deve possuir:
  - ID único
  - Dois times participantes
  - Status
  - Placar

- Os status possíveis de uma partida são:
  - AGENDADA
  - EM_ANDAMENTO
  - FINALIZADA

- Uma partida finalizada não pode ser reiniciada.

- Ao finalizar uma partida:
  - o vencedor é definido automaticamente
  - o status muda para FINALIZADA

---

## 6. Torneios

- Todo torneio deve possuir:
  - ID único
  - Nome
  - Tipo de torneio

- Os tipos disponíveis são:
  - PONTOS_CORRIDOS
  - ELIMINACAO_SIMPLES

- Um torneio pode possuir múltiplos times.

- Um torneio pode possuir múltiplas partidas.

- Os confrontos são gerados automaticamente pelo sistema.

---

## 7. Ranking

- O ranking é atualizado com base nos resultados das partidas.

- Regras de pontuação:
  - Vitória = 3 pontos
  - Derrota = 0 pontos

- O ranking é ordenado pela quantidade de pontos.

---

## 8. Estatísticas

- O sistema registra:
  - partidas jogadas
  - MVPs
  - KD Ratio

- O KD Ratio é calculado pela fórmula:

```text
kills / deaths
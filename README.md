# Chess Game Pygame ES II
[![](https://img.shields.io/badge/Python-v3.8.6-blue?logo=python)](https://www.python.org/)
[![](https://img.shields.io/badge/pygame-v2.0-yellow)](https://www.pygame.org/)

Jogo desenvolvido em [Python](https://www.python.org/) utilizando o modulo de jogos [pygame](https://www.pygame.org/). O jogo está sendo desenvolvido para o curso de Engenharia de Software II.

## Sobre o Jogo

Nada mais que um simples jogo de xadrez.
O computador escolhe as jogadas através do algoritmo [Minimax](https://pt.wikipedia.org/wiki/Minimax) e otimizado para fazer melhores escolhas com o algoritmo de otimização [Alpha-Beta-Pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).

### Como Jogar

Ao selecionar uma peça do tabuleiro com o mouse aparecerá as opções de jogadas possíveis para a peça, ao selecionar o quadrado para qual deseja mover a peça o jogo altera as posições e passa a vez do jogo para máquina e por aí em diante. As regras são as mesmas de um jogo de xadrez clássico.

## Como jogar localmente

<details>
<summary>Exemplo de uso</summary>

**Clone e install**

```bash
git clone git@github.com:Zamp98/chessPygame.git
cd chessPygame
source venv/Scripts/activate
pip install pygame
```

**Iniciar jogo local**

```bash
python3 main.py
#ou
python main.py
```

## Como iniciar o Teste de Unidade

O teste de unidadde consiste em um teste de entrada e saida do jogo. todos os testes precisam retornar ok.

```bash
python3 -m unittest -v unitTestChess.Test
```
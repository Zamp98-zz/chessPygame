# importando todos os modulos menos a main
import pygame
import unittest
from modules.board import *
from modules.oponent import *
from modules.pieces import *


class Test(unittest.TestCase):
    # iniciando o pygame para poder iniciar os testes
    pygame.init()
    screen = pygame.display.set_mode((500, 500))  # criando tela
    board = Board()  # dando init no tabuleiro

    def test_get_board(self):
        # testando se o tabuleiro criado é realmente um lista ou não
        self.assertIsInstance(self.board.getBoard(), list)

    def test_move_piece(self):
        # cria uma peça do tipo pião na matriz com posição [1,1]
        piece = Pawn("white", 1, 1)
        # checando se o retorno da função é realmente uma tupla
        self.assertIsInstance(self.board.movePiece(piece, 0, 0), tuple)

    def test_piece_promotion(self):
        # cria uma peça do tipo pião na matriz com posição [1,1]
        piece = Pawn("white", 1, 1)
        # checando se a peça quando movida para uma posição com y = 1 ela retorna True
        self.assertTrue(checkPiecePromotion(piece, 0))
        # checando se a peça quando movida para uma posição com y = 2 ela retorna False
        self.assertFalse(checkPiecePromotion(piece, 2))

    def test_capture_tile(self):
        # checa se peça branca pode ir para posição de uma peça preta
        self.assertTrue(captureTile("white", 0, 0, self.board))
        # checa se quadrado está vazio
        self.assertFalse(captureTile("white", 3, 3, self.board))
        # checa se peça branca pode ir para posição de uma peça branca
        self.assertFalse(captureTile("white", 7, 7, self.board))

    def test_move_check(self):
        self.assertFalse(moveCheck("white", 8, 8, self.board)
                         )  # checa movimentação invalida
        # checa movimentação invalida
        self.assertFalse(moveCheck("white", -1, -1, self.board))
        # checa movimentação para um campo vazio
        self.assertTrue(moveCheck("white", 3, 3, self.board))
        # checa movimentação para um campo com peça rival
        self.assertTrue(moveCheck("white", 0, 0, self.board))
        # checa movimentação para um campo com peça da mesma cor
        self.assertFalse(moveCheck("white", 6, 6, self.board))


if __name__ == '__main__':
    unittest.main()

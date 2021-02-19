from modules.pieces import *


class Board:
    def __init__(self):
        self.empty = [[None for x in range(8)] for y in range(8)]
        self.black_king = King("black", 0, 4)
        self.white_king = King("white", 7, 4)
        self.white_rook_left = Rook("white", 7, 0)
        self.white_rook_right = Rook("white", 7, 7)
        self.black_rook_left = Rook("black", 0, 0)
        self.black_rook_right = Rook("black", 0, 7)
        self.array = [
            [self.black_rook_left, Knight("black", 0, 1), Bishop("black", 0, 2), Queen("black", 0, 3),
                self.black_king, Bishop("black", 0, 5), Knight("black", 0, 6), self.black_rook_right],
            [Pawn("black", 1, i) for i in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            [Pawn("white", 6, i) for i in range(8)],
            [self.white_rook_left, Knight("white", 7, 1), Bishop("white", 7, 2), Queen("white", 7, 3),
                self.white_king, Bishop("white", 7, 5), Knight("white", 7, 6), self.white_rook_right]
        ]

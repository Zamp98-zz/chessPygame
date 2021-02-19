from modules.pieces import *


class Board:
    def __init__(self):
        self.empty = [[None for x in range(8)] for y in range(8)]
        self.blackKing = King("black", 0, 4)
        self.whiteKing = King("white", 7, 4)
        self.whiteRookLeft = Rook("white", 7, 0)
        self.whiteRookRight = Rook("white", 7, 7)
        self.blackRookLeft = Rook("black", 0, 0)
        self.blackRookRight = Rook("black", 0, 7)
        self.array = [
            [self.blackRookLeft, Knight("black", 0, 1), Bishop("black", 0, 2), Queen("black", 0, 3),
                self.blackKing, Bishop("black", 0, 5), Knight("black", 0, 6), self.blackRookRight],
            [Pawn("black", 1, i) for i in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            [Pawn("white", 6, i) for i in range(8)],
            [self.whiteRookLeft, Knight("white", 7, 1), Bishop("white", 7, 2), Queen("white", 7, 3),
                self.whiteKing, Bishop("white", 7, 5), Knight("white", 7, 6), self.whiteRookRight]
        ]

from modules.pieces import *


def checkPiecePromotion(piece, y):
    if piece.color == "white":
        row = 1
        inc = -1
    elif piece.color == "black":
        row = 6
        inc = 1
    if type(piece) == Pawn and piece.y == row and y == piece.y + inc:
        return True
    else:
        return False


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

        self.score = 0

        self.pieceValues = {King: 200, Queen: 10,
                            Rook: 5, Knight: 3, Bishop: 3, Pawn: 1}

    def getBoard(self):
        return self.array

    def movePiece(self, piece, y, x, special=False, np=False):
        promotion = checkPiecePromotion(piece, y)
        oldx = piece.x
        oldy = piece.y
        piece.x = x
        piece.y = y
        piece.rect.x = x * 60
        piece.rect.y = y * 60
        self.array[oldy][oldx] = None

        if promotion and not np:
            self.array[y][x] = Queen(piece.color, y, x)
            if piece.color == "white":
                self.score -= 9
            elif piece.color == "black":
                self.score += 9

            return self.array[y][x], piece
        else:
            self.array[y][x] = piece
            piece.unsethighlighted()

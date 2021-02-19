from modules.board import *


def matrixToTuple(array, arrayEmpty):
    for i in range(8):
        arrayEmpty[i] = tuple(array[i])
    return tuple(arrayEmpty)


def generatePossibleMoves(board, color, attc=False):
    if attc:
        moves = set()
    else:
        moves = dict()

    for j in range(8):
        for i in range(8):
            piece = board.array[i][j]
            if piece != None and piece.color == color:
                legalMoves = piece.generatedLegalMoves(board)
                if legalMoves and not attc:
                    moves[(i, j)] = legalMoves
                elif legalMoves and attc:
                    moves = moves.union(legalMoves)

    return moves


def minimax(board, depth, alpha, beta, maximizing, lastMove):
    boardTuple = matrixToTuple(board.array, board.empty)

    if boardTuple in lastMove and depth != 3:
        return lastMove[boardTuple], 0

    if depth == 0:
        lastMove[boardTuple] = board.score
        return board.score, 0

    if maximizing:
        bestValue = float("-inf")
        blackMoves = generatePossibleMoves(board, "b")

        for start, moveSet in blackMoves.items():
            for end in moveSet:

                piece = board.array[start[0]][start[1]]
                dest = board.array[end[0]][end[1]]

                pawnPromotion = board.movePiece(piece, end[0], end[1], False)

                attacked = generatePossibleMoves(board, "w", True)
                if (board.blackKing.y, board.blackKing.x) in attacked:
                    board.movePiece(piece, start[0], start[1], False, True)
                    board.array[end[0]][end[1]] = dest
                    if pawnPromotion:
                        board.score -= 9
                    continue

                if dest != None:
                    board.score += board.pieceValueDict[type(dest)]

                v, __ = minimax(board, depth - 1, alpha, beta, False, lastMove)

                board.movePiece(piece, start[0], start[1], False, True)
                board.array[end[0]][end[1]] = dest

                if pawnPromotion:
                    board.score -= 9

                if dest != None:
                    board.score -= board.pieceValueDict[type(dest)]

                if v >= bestValue:
                    move = (start, (end[0], end[1]))

                bestValue = max(bestValue, v)
                alpha = max(alpha, bestValue)

                if beta <= alpha:
                    return bestValue, move
        try:
            return bestValue, move
        except:
            return bestValue, 0

    else:
        bestValue = float("inf")
        whiteMoves = generatePossibleMoves(board, "w")

        for start, moveSet in whiteMoves.items():
            for end in moveSet:

                piece = board.array[start[0]][start[1]]
                dest = board.array[end[0]][end[1]]
                pawnPromotion = board.movePiece(piece, end[0], end[1], False)

                attacked = generatePossibleMoves(board, "b", True)
                if (board.whiteKing.y, board.whiteKing.x) in attacked:
                    board.movePiece(piece, start[0], start[1], False, True)
                    board.array[end[0]][end[1]] = dest
                    if pawnPromotion:
                        board.score += 9
                    continue

                if dest != None:
                    board.score -= board.pieceValueDict[type(dest)]

                v, __ = minimax(board, depth - 1, alpha, beta, True, lastMove)

                bestValue = min(v, bestValue)
                beta = min(beta, bestValue)

                board.movePiece(piece, start[0], start[1], False, True)
                board.array[end[0]][end[1]] = dest
                if pawnPromotion:
                    board.score += 9
                if dest != None:
                    board.score += board.pieceValueDict[type(dest)]

                if beta <= alpha:
                    return bestValue, 0

        return bestValue, 0

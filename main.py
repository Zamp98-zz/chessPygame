# import the pygame module, so you can use it
import pygame
from modules.board import *
from modules.oponent import *

# define a main function


def main():
    pygame.init()
    logo = pygame.image.load("images/blackQueen.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")


screen = pygame.display.set_mode((500, 500))

bg = pygame.image.load("images/chessBoard.png").convert()

board = Board()

global allSpritesList, sprites
allSpritesList = pygame.sprite.Group()
sprites = [piece for row in board.array for piece in row if piece]
allSpritesList.add(sprites)

# draw the sprites
allSpritesList.draw(screen)

# 60FPS PC Master Race
clock = pygame.time.Clock()

# define a variable to control the main loop
running = True

Rects = pygame.sprite.Group()


def tileSelected():
    x, y = pygame.mouse.get_pos()
    x = x // 60
    y = y // 60
    return (y, x)

gameState = 0
pieceSelected = False
player = "white"
trans_table = dict()

# main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False
        if gameState == 0:
            '''        self.sprite = pygame.image.load("templates/vertex.png")
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
        self.rect = self.sprite.get_rect()#tem que pegar a coordenada do sprite e setar de acordo com a coordenada nova do vértice
        self.rect.x, self.rect.y = x * 60, y * 60
        self.x = x
        self.y = y'''

            background = pygame.image.load("images/mainScreen.png")
            background = pygame.transform.scale(background, (500, 500))
            start = pygame.image.load("images/playervsIA.png")
            sRect = start.get_rect()

            sRect.x = 150
            sRect.y = 125

            quitButton = pygame.image.load("images/quit.png")
            qRect = quitButton.get_rect()
            qRect.x = 150
            qRect.y = 250
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y positions of the mouse click
                if sRect.collidepoint(event.pos):
                    gameState = 1
                elif qRect.collidepoint(event.pos):
                    running = False

            screen.blit(background, (0, 0))
            screen.blit(start, sRect)
            screen.blit(quitButton, qRect)
            pygame.display.flip()
            clock.tick(60)
        elif gameState == 1:
            if player == "white":
                if event.type == pygame.MOUSEBUTTONDOWN and not pieceSelected:
                    # Set the x, y positions of the mouse click
                    x, y = event.pos
                    clickedSprites = [
                        s for s in sprites if s.rect.collidepoint(event.pos)]
                    if(len(clickedSprites) > 0) and clickedSprites[0].color == "white":
                        if not clickedSprites[0].highlighted:
                            clickedSprites[0].sethighlighted()

                        for s in sprites:  # allow only one highlighted
                            if s != clickedSprites[0] and s.highlighted:
                                s.unsethighlighted()
                                Rects = set()

                        pieceMoves = clickedSprites[0].genLegalMoves(board)
                        pieceSelected = True

                        for move in pieceMoves:
                            movementRect = MovementRect(move[0], move[1], screen)
                            Rects.add(movementRect)

                elif event.type == pygame.MOUSEBUTTONDOWN and pieceSelected:
                    tile = tileSelected()
                    pieceSelected = False
                    Rects = set()
                    specialMovesRoque = specialMoveGen(board, "white")
                    enPassant = checkEnPassant(board, clickedSprites[0], "white")

                    if tile in pieceMoves:
                        oldx = clickedSprites[0].x
                        oldy = clickedSprites[0].y
                        dest = board.array[tile[0]][tile[1]]

                        piecePromotion = board.movePiece(
                            clickedSprites[0], tile[0], tile[1])

                        if piecePromotion:
                            allSpritesList.add(piecePromotion[0])
                            sprites.append(piecePromotion[0])
                            allSpritesList.remove(piecePromotion[1])
                            sprites.remove(piecePromotion[1])

                        if dest:
                            allSpritesList.remove(dest)
                            sprites.remove(dest)

                        attacked = generatePossibleMoves(board, "black", True)
                        if (board.whiteKing.y, board.whiteKing.x) not in attacked:
                            selected = False
                            player = "black"

                            if dest:
                                board.score -= board.pieceValues[type(dest)]

                        else:  # THIS MOVE IS IN CHECK, we have to reverse it
                            board.movePiece(clickedSprites[0], oldy, oldx)
                            if type(clickedSprites[0]) == King or type(clickedSprites[0]) == Rook:
                                clickedSprites[0].moved = False
                            board.array[tile[0]][tile[1]] = dest
                            if dest:  # if dest not None
                                allSpritesList.add(dest)
                                sprites.append(dest)
                            if piecePromotion:
                                allSpritesList.add(piecePromotion[1])
                                sprites.append(piecePromotion[1])
                            clickedSprites[0].sethighlighted()

                            # different sidemenus depend on whether or not you're
                            # currently in check
                            if checkWhite:
                                pygame.display.update()
                                pygame.time.wait(1000)
                            else:
                                pygame.display.update()
                                pygame.time.wait(1000)


                    elif (clickedSprites[0].y, clickedSprites[0].x) == tile:
                        clickedSprites[0].unsethighlighted()
                        selected = False

                    elif enPassant:
                        if(tile[0] == clickedSprites[0].y-1 and tile[1] == clickedSprites[0].x+1 or tile[0] == clickedSprites[0].y-1 and tile[1] == clickedSprites[0].x-1):
                            special = "EP"
                            board.movePiece(
                                clickedSprites[0], tile[0], tile[1], special)

                            selected = False
                            player = "black"

                    elif specialMovesRoque and tile in specialMovesRoque:
                        special = specialMovesRoque[tile]
                        if (special == "CR" or special == "CL") and type(clickedSprites[0]) == King:
                            board.movePiece(
                                clickedSprites[0], tile[0], tile[1], special)
                            selected = False
                            player = "black"

                        else:
                            pygame.display.update()
                            pygame.time.wait(1000)

                    elif (clickedSprites[0].y, clickedSprites[0].x) == tile:
                        clickedSprites[0].unsethighlighted()
                        selected = False


            elif player == 'black':
                value, move = minimax(board, 3, float(
                    "-inf"), float("inf"), True, trans_table)

                if value == float("-inf") and move == 0:
                    print("AI checkmate")
                    player = 'white'
                    running = True

                else:
                    start = move[0]
                    end = move[1]
                    piece = board.array[start[0]][start[1]]
                    dest = board.array[end[0]][end[1]]

                    piecePromotion = board.movePiece(piece, end[0], end[1])
                    if piecePromotion:
                        allSpritesList.add(piecePromotion[0])
                        sprites.append(piecePromotion[0])
                        allSpritesList.remove(piecePromotion[1])
                        sprites.remove(piecePromotion[1])

                    if dest:
                        allSpritesList.remove(dest)
                        sprites.remove(dest)
                        board.score += board.pieceValues[type(dest)]

                    player = 'white'
                    attacked = generatePossibleMoves(board, "black", True)
                    if (board.whiteKing.y, board.whiteKing.x) in attacked:
                        checkWhite = True
                    else:
                        checkWhite = False

                if value == float("inf"):
                    print("Player checkmate")
                    running = False
                    player = 'AI'

            allSpritesList = pygame.sprite.Group()
            sprites = [piece for row in board.array for piece in row if piece]
            allSpritesList.add(sprites)
            allSpritesList.add(Rects)

            # draw the sprites
            allSpritesList.draw(screen)
            screen.blit(bg, (0, 0))
            allSpritesList.draw(screen)
            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    main()

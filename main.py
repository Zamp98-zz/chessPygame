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

pieceSelected = False

# main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False
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


            elif (clickedSprites[0].y, clickedSprites[0].x) == tile:
                clickedSprites[0].unsethighlighted()
                selected = False

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

# import the pygame module, so you can use it
import pygame
from modules.board import *

# define a main function


def main():
    pygame.init()
    logo = pygame.image.load("images/blackQueen.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")


screen = pygame.display.set_mode((640, 500))
bg = pygame.image.load("images/chessBoard.png").convert()

board = Board()

global all_sprites_list, sprites
all_sprites_list = pygame.sprite.Group()
sprites = [piece for row in board.array for piece in row if piece]
all_sprites_list.add(sprites)

# draw the sprites
all_sprites_list.draw(screen)

# 60FPS PC Master Race
clock = pygame.time.Clock()

# define a variable to control the main loop
running = True


# main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False

    screen.blit(bg, (0, 0))
    all_sprites_list.draw(screen)
    pygame.display.update()
    clock.tick(60)

if __name__ == "__main__":
    main()

# import the pygame module, so you can use it
import pygame
from modules.board import *

# define a main function


def main():
    pygame.init()
    logo = pygame.image.load("images/blackQueen.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")


screen = pygame.display.set_mode((500, 500))
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
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y positions of the mouse click
            x, y = event.pos
            clicked_sprites = [s for s in sprites if s.rect.collidepoint(event.pos)]
            if(len(clicked_sprites) > 0):
                clicked_sprites[0].sethighlighted()


                for s in sprites:#allow only one highlighted
                    if s != clicked_sprites[0] and s.highlighted:
                       s.unsethighlighted()
    all_sprites_list = pygame.sprite.Group()
    sprites = [piece for row in board.array for piece in row if piece]
    all_sprites_list.add(sprites)

    # draw the sprites
    all_sprites_list.draw(screen)
    screen.blit(bg, (0, 0))
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

if __name__ == "__main__":
    main()

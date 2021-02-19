import pygame


class Piece(pygame.sprite.Sprite):
    def __init__(self, color, y, x):
        super().__init__()
        self.color = color
        self.x = x
        self.y = y
        self.image = pygame.Surface((60, 60), pygame.SRCALPHA, 32)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x * 60, y * 60
        self.highlighed = False


class Pawn(Piece):
    def __init__(self, color, y, x):
        super().__init__(color, y, x)
        self.symbol = "P"
        self.sprite = pygame.image.load("images/{}Pawn.png".format(self.color))
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
        self.image.blit(self.sprite, (5, 5))


class Rook(Piece):
    def __init__(self, color, y, x):
        super().__init__(color, y, x)
        self.sprite = pygame.image.load("images/{}Rook.png".format(self.color))
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
        self.symbol = "R"
        self.image.blit(self.sprite, (5, 5))
        self.moved = False


class Bishop(Piece):
    def __init__(self, color, y, x):
        super().__init__(color, y, x)
        self.sprite = pygame.image.load(
            "images/{}Bishop.png".format(self.color))
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
        self.symbol = "B"
        self.image.blit(self.sprite, (5, 5))


class Knight(Piece):
    def __init__(self, color, y, x):
        super().__init__(color, y, x)
        self.sprite = pygame.image.load(
            "images/{}Knight.png".format(self.color))
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
        self.symbol = "N"
        self.image.blit(self.sprite, (5, 5))


class King(Piece):
    def __init__(self, color, y, x):
        super().__init__(color, y, x)
        self.sprite = pygame.image.load("images/{}King.png".format(self.color))
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
        self.symbol = "K"
        self.image.blit(self.sprite, (5, 5))
        self.moved = False


class Queen(Piece):
    def __init__(self, color, y, x):
        super().__init__(color, y, x)
        self.sprite = pygame.image.load(
            "images/{}Queen.png".format(self.color))
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
        self.symbol = "Q"
        self.image.blit(self.sprite, (5, 5))
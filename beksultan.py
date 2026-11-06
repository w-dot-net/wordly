"""Мейрамбай Бексұлтан — Tile және Board."""
import pygame


class Tile:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 45, 45)
        self.letter = ""
        self.color = (58, 60, 72)

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.letter != "":
            text = font.render(self.letter.upper(), True, (255, 255, 255))
            text_rect = text.get_rect(center=self.rect.center)
            screen.blit(text, text_rect)


class Board:
    def __init__(self):
        self.tiles = []
        for row in range(6):
            for col in range(5):
                self.tiles.append(Tile(177 + col * 50, 15 + row * 50))

    def tile(self, row, col):
        return self.tiles[row * 5 + col]

    def draw(self, screen, font):
        for tile in self.tiles:
            tile.draw(screen, font)

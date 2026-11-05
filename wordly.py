# Wordly - 7-команданың жобасы
import pygame
import random

WIDTH, HEIGHT = 600, 400

WORDS = ["apple", "house", "table", "tiger", "robot",
         "plant", "cloud", "smile", "train", "brick",
         "snake", "ocean", "chair", "storm", "glass"]

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class WordList:
    def __init__(self, words):
        self.words = words

    def random_word(self):
        i = random.randint(0, len(self.words) - 1)
        return self.words[i]


class Tile:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 45, 45)
        self.letter = ""
        self.color = (58, 60, 72)

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.letter != "":
            text = font.render(self.letter.upper(), True, (255, 255, 255))
            screen.blit(text, (self.rect.x + 16, self.rect.y + 8))


class Board:
    def __init__(self):
        self.tiles = []
        for row in range(6):
            for col in range(5):
                self.tiles.append(Tile(177 + col * 50, 15 + row * 50))

    def tile(self, row, col):
        return self.tiles[row * 5 + col]

    def draw(self, screen, font):
        for t in self.tiles:
            t.draw(screen, font)


class Game:
    def __init__(self):
        self.words = WordList(WORDS)
        self.secret = self.words.random_word()
        self.board = Board()
        self.row = 0
        self.current = ""
        self.over = False
        self.won = False

    def on_key(self, event):
        if self.over:
            return
        if event.key == pygame.K_RETURN:
            self.submit()
        elif event.key == pygame.K_BACKSPACE:
            new = ""
            for i in range(len(self.current) - 1):
                new = new + self.current[i]
            self.current = new
        elif pygame.K_a <= event.key <= pygame.K_z:
            if len(self.current) < 5:
                self.current = self.current + ALPHABET[event.key - pygame.K_a]

    def submit(self):
        if len(self.current) != 5:
            return


        colors = [0, 0, 0, 0, 0]
        used = [False, False, False, False, False]
        for i in range(5):
            if self.current[i] == self.secret[i]:
                colors[i] = 2
                used[i] = True


        for i in range(5):
            if colors[i] != 2:
                for j in range(5):
                    if used[j] == False and self.secret[j] == self.current[i]:
                        colors[i] = 1
                        used[j] = True

        for col in range(5):
            tile = self.board.tile(self.row, col)
            tile.letter = self.current[col]
            if colors[col] == 2:
                tile.color = (106, 170, 100)
            elif colors[col] == 1:
                tile.color = (201, 180, 88)
            else:
                tile.color = (120, 124, 126)

        self.row = self.row + 1
        if self.current == self.secret:
            self.over = True
            self.won = True
        elif self.row >= 6:
            self.over = True
        self.current = ""

    def draw(self, screen, font):
        screen.fill((15, 15, 35))

        if not self.over:
            for col in range(5):
                tile = self.board.tile(self.row, col)
                if col < len(self.current):
                    tile.letter = self.current[col]
                    tile.color = (68, 70, 84)
                else:
                    tile.letter = ""
                    tile.color = (58, 60, 72)

        self.board.draw(screen, font)

        title = font.render("Wordly: 5 әріптік сөзді тап", True, (255, 255, 255))
        screen.blit(title, (177, 320))
        hint = font.render(f"Әрекет {self.row + 1}/6. Enter — тексеру", True, (255, 255, 255))
        screen.blit(hint, (177, 352))

        if self.over:
            pygame.draw.rect(screen, (42, 45, 60), (90, 120, 420, 70))
            if self.won:
                msg = font.render("ЖЕҢІС! Жаңа ойын: R", True, (106, 170, 100))
            else:
                msg = font.render(f"Ойын бітті. Сөз: {self.secret.upper()}. R — жаңа ойын", True, (201, 180, 88))
            screen.blit(msg, (115, 145))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordly — 7-команда")
clock = pygame.time.Clock()
font = pygame.font.Font(r"C:\Windows\Fonts\segoeui.ttf", 26)

game = Game()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r and game.over:
            game = Game()
        elif event.type == pygame.KEYDOWN:
            game.on_key(event)

    game.draw(screen, font)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

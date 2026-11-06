"""Тлеуберген Қыран — WordList және Game логикасы."""
import random
from beksultan import Board

WORDS = ["apple", "house", "table", "tiger", "robot",
         "plant", "cloud", "smile", "train", "brick",
         "snake", "ocean", "chair", "storm", "glass"]


class WordList:
    def __init__(self, words):
        self.words = words

    def random_word(self):
        i = random.randint(0, len(self.words) - 1)
        return self.words[i]


class Game:
    def __init__(self):
        self.words = WordList(WORDS)
        self.secret = self.words.random_word()
        self.board = Board()
        self.row = 0
        self.current = ""
        self.over = False
        self.won = False

    def submit(self):
        if self.over or len(self.current) != 5:
            return

        colors = [0, 0, 0, 0, 0]
        used = [False, False, False, False, False]

        # Алдымен жасыл: әріп пен орны дұрыс.
        for i in range(5):
            if self.current[i] == self.secret[i]:
                colors[i] = 2
                used[i] = True

        # Сосын сары: әріп бар, бірақ басқа орында.
        for i in range(5):
            if colors[i] != 2:
                for j in range(5):
                    if not used[j] and self.secret[j] == self.current[i]:
                        colors[i] = 1
                        used[j] = True
                        break

        for col in range(5):
            tile = self.board.tile(self.row, col)
            tile.letter = self.current[col]
            if colors[col] == 2:
                tile.color = (106, 170, 100)
            elif colors[col] == 1:
                tile.color = (201, 180, 88)
            else:
                tile.color = (120, 124, 126)

        self.row += 1
        if self.current == self.secret:
            self.over = True
            self.won = True
        elif self.row >= 6:
            self.over = True
        self.current = ""

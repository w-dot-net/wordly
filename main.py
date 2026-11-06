"""Әскер Әліби — пернетақта, экран, ойын циклі және тестілеу."""
import pygame
from kyran import Game

WIDTH, HEIGHT = 600, 400
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def on_key(game, event):
    if game.over:
        return
    if event.key == pygame.K_RETURN:
        game.submit()
    elif event.key == pygame.K_BACKSPACE:
        game.current = game.current[:-1]
    elif pygame.K_a <= event.key <= pygame.K_z:
        if len(game.current) < 5:
            game.current += ALPHABET[event.key - pygame.K_a]


def draw(game, screen, font):
    screen.fill((15, 15, 35))

    if not game.over:
        for col in range(5):
            tile = game.board.tile(game.row, col)
            if col < len(game.current):
                tile.letter = game.current[col]
                tile.color = (68, 70, 84)
            else:
                tile.letter = ""
                tile.color = (58, 60, 72)

    game.board.draw(screen, font)

    title = font.render("Wordly: 5 әріптік сөзді тап", True, (255, 255, 255))
    screen.blit(title, (177, 320))
    hint = font.render(f"Әрекет {min(game.row + 1, 6)}/6. Enter — тексеру", True, (255, 255, 255))
    screen.blit(hint, (177, 352))

    if game.over:
        pygame.draw.rect(screen, (42, 45, 60), (60, 120, 480, 70))
        if game.won:
            message = "ЖЕҢІС! Жаңа ойын: R"
            color = (106, 170, 100)
        else:
            message = f"Ойын бітті. Сөз: {game.secret.upper()}. R — жаңа ойын"
            color = (201, 180, 88)
        msg = font.render(message, True, color)
        screen.blit(msg, msg.get_rect(center=(300, 155)))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Wordly — 7-команда ВОЗДУХ")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("segoeui", 23)
    game = Game()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r and game.over:
                game = Game()
            elif event.type == pygame.KEYDOWN:
                on_key(game, event)

        draw(game, screen, font)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

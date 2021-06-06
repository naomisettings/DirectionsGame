import pygame
import game.game_config as gc

from pygame import display, event, image

pygame.init()
display.set_caption('Directions')
screen = display.set_mode((0, 0), pygame.FULLSCREEN)

board = image.load('assets/board.png')
screen.blit(pygame.transform.scale(board, screen.get_size()), (0, 0))

#board = pygame.transform.scale(board, (720, 720))
#board_rect = board.get_rect(center=(1024,560))

running = True

while running:

    current_events = event.get()
    for e in current_events:
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False

    #screen.blit(board, board_rect)
    display.flip()

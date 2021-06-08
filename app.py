import pygame
import game_config as gc
from box import Box

from pygame import display, event, image


def find_index_from_xy(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return row, col, index

pygame.init()
display.set_caption('Directions')
screen = display.set_mode((0, 0), pygame.FULLSCREEN)

board = image.load('assets/board.png')
screen.blit(pygame.transform.scale(board, screen.get_size()), (0, 0))

#board = pygame.transform.scale(board, (720, 720))
#board_rect = board.get_rect(center=(1024,560))

tiles = [Box(i) for i in range(0, gc.NUM_TILES_TOTAL)]

running = True

while running:

    current_events = event.get()
    for e in current_events:
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row, col, index = find_index_from_xy(mouse_x, mouse_y)

    #Display boxes
    #screen.fill((255, 255, 255))
    screen.blit(board, [0, 0])
  
    for i, tile in enumerate(tiles):
        screen.blit(tile.image, (tile.col * gc.IMAGE_SIZE + gc.MARGIN + 620, tile.row * gc.IMAGE_SIZE + gc.MARGIN + 165))
        
    display.flip()

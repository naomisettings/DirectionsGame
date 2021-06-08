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
#tiles = dict((Box(i), 0) for i in range(0, gc.NUM_TILES_TOTAL))
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
            moved = False
            for i, tile in enumerate(tiles):
                if (not(tile.row == 0 and tile.col == 4) and not(tile.row ==  4 and tile.col == 0)):
                    if (tile.row == 0 and tile.col != 3 and moved == False):   
                        tile.col += 1
                        moved = True
                    elif (tile.col == 3 and tile.row == 0 and moved == False):
                        tile.row += 1 
                        tile.col += 1
                        moved = True
                    if (tile.col == 4 and tile.row != 4 and moved == False):
                        tile.row += 1
                        moved = True
                    elif(tile.row == 4 and tile.col != 0 and moved == False):
                        tile.col -= 1
                        tile.row -= 1
                moved = False    
            for i, tile in enumerate(tiles):
                screen.blit(tile.image, (tile.col * gc.IMAGE_SIZE + gc.MARGIN + 620, tile.row * gc.IMAGE_SIZE + gc.MARGIN + 165))
    #Display boxes
    #screen.fill((255, 255, 255))
    screen.blit(board, [0, 0])
  
    for i, tile in enumerate(tiles):
        screen.blit(tile.image, (tile.col * gc.IMAGE_SIZE + gc.MARGIN + 620, tile.row * gc.IMAGE_SIZE + gc.MARGIN + 165))
    print('x')
    display.flip()


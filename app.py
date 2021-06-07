import pygame
import game.game_config as gc
from game.box import Box


from pygame import display, event, image

pygame.init()
display.set_caption('Directions')
screen = display.set_mode((0, 0), pygame.FULLSCREEN)

board = image.load('assets/board.png')
screen.blit(pygame.transform.scale(board, screen.get_size()), (0, 0))

#board = pygame.transform.scale(board, (720, 720))
#board_rect = board.get_rect(center=(1024,560))

tiles = [Box(i) for i in range(0, gc.NUM_TILES_TOTAL)]
x = 0
#for (x in range(gc.NUM_TILES_TOTAL))



running = True

while running:

    current_events = event.get()
    for e in current_events:
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False


    # Display boxes
    screen.fill((255, 255, 255))
"""
    for i, tile in enumerate(tiles):
        current_image = tile.image if i in current_images_displayed else tile.box
        if not tile.skip:
            screen.blit(current_image, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
        else:
            total_skipped += 1
    display.flip()
"""
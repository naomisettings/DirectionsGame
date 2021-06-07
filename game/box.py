import random
import os
import game.game_config as gc

from pygame import image, transform

BOX_COUNT_BORDER = dict((a, 0) for a in gc.ASSET_FILES_BORDER)
BOX_COUNT_MIDDLE = dict((a, 0) for a in gc.ASSET_FILES_MIDDLE)
BOX_COUNT_CENTER = dict((a, 0) for a in gc.ASSET_FILES_CENTER)


class Box:
    def __init__(self, index):

        self.index = index
        #self.name = random.choice(available_animals())
        self.image_path_border = os.path.join(gc.ASSET_DIR_BORDER, self.name)
        self.image_path_middle = os.path.join(gc.ASSET_DIR_MIDDLE, self.name)
        self.image_path_center = os.path.join(gc.ASSET_DIR_CENTER, self.name)
        self.row = index // gc.NUM_TILES_SIDE
        self.col = index % gc.NUM_TILES_SIDE
        self.skip = False

        self.image_border = image.load(self.image_path_border)
        self.image_border = image.load(self.image_path_middle)
        self.image_border = image.load(self.image_path_center)

        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2 * gc.MARGIN, gc.IMAGE_SIZE - 2 * gc.MARGIN))
        self.box.fill((200, 200, 200))

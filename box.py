import random
import os
import game_config as gc

from pygame import image, transform

box_border = [a for a in gc.ASSET_FILES_BORDER]
box_middle = [a for a in gc.ASSET_FILES_MIDDLE]
box_center = [a for a in gc.ASSET_FILES_CENTER]
box_start_end = [a for a in gc.ASSET_FILES_START_END]

class Box(object):
    def __init__(self, index):

        self.index = index
        
        self.row = index // gc.NUM_TILES_SIDE
        self.col = index % gc.NUM_TILES_SIDE
        
        name = ''
        if (self.row == 4 and self.col == 0):
            name = '0.png'
        elif (self.row == 0 and self.col == 4):
            name = '1.png'
        elif (self.row == 0 or self.col == 0 or self.row == 4 or self.col == 4):
            name = random.sample(box_border, gc.NUM_TILES_BORDER)[0]
        elif (self.row == 1 or self.col == 1 or self.row == 3 or self.col == 3):
            name = random.sample(box_middle, gc.NUM_TILES_MIDDLE)[0] 
        else:
            name = box_center[0]

        self.name = name

        self.image_path_border = os.path.join(gc.ASSET_DIR_BORDER, self.name)
        self.image_path_middle = os.path.join(gc.ASSET_DIR_MIDDLE, self.name)
        self.image_path_center = os.path.join(gc.ASSET_DIR_CENTER, self.name)
        self.image_path_start_end = os.path.join(gc.ASSET_DIR_START_END, self.name)


        self.skip = False
        
        if (self.name in box_start_end):
            self.image_start_end = image.load(self.image_path_start_end)
            self.image = self.image_start_end
        elif (self.name in box_border):
            self.image_border = image.load(self.image_path_border)
            self.image = self.image_border
        elif (self.name in box_middle):
            self.image_middle = image.load(self.image_path_middle)
            self.image = self.image_middle
        else:
            print(self.image_path_center)
            self.image_center = image.load(self.image_path_center)
            self.image = self.image_center

        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2 * gc.MARGIN, gc.IMAGE_SIZE - 2 * gc.MARGIN))

    def row(self, r): 
         self._row = r 

    def col(self, c): 
         self._col = c 
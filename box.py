import random
import os
import game_config as gc

from pygame import image, transform

box_border = [a for a in gc.ASSET_FILES_BORDER]
box_middle = [a for a in gc.ASSET_FILES_MIDDLE]
box_center = [a for a in gc.ASSET_FILES_CENTER]
box_start_end = [a for a in gc.ASSET_FILES_START_END]

random.shuffle(box_border)
random.shuffle(box_middle)

class Box(object):
    
    def __init__(self, index, count_border, count_middle):

        self.first_time = True

        self.index = index
        self.row = index // gc.NUM_TILES_SIDE
        self.col = index % gc.NUM_TILES_SIDE

        name = ''
        if (index == 20):
            name = '0.png'
        elif (index == 4):
            name = '1.png'
        elif index == 0 or index == 1 or index== 2 or index == 3 or index == 5 or index == 9 or index == 10 or index == 14 or index == 15 or index == 19 or index == 21 or index == 22 or index == 23 or index == 24:
            name = box_border[count_border]
        elif index == 6 or index == 7 or index == 8 or index == 9 or index == 11  or index == 13 or index == 16 or index == 17 or index == 18:
            name = box_middle[count_middle]
        elif index == 12:
            name = box_center[0]
        self.name = name
        self.image_path_border = os.path.join(gc.ASSET_DIR_BORDER, self.name)
        self.image_path_middle = os.path.join(gc.ASSET_DIR_MIDDLE, self.name)
        self.image_path_center = os.path.join(gc.ASSET_DIR_CENTER, self.name)
        self.image_path_start_end = os.path.join(gc.ASSET_DIR_START_END, self.name)

        if self.name in box_start_end:
            self.image_start_end = image.load(self.image_path_start_end)
            self.image = self.image_start_end
        elif self.name in box_border:
            self.image_border = image.load(self.image_path_border)
            self.image = self.image_border
        elif self.name in box_middle:
            self.image_middle = image.load(self.image_path_middle)
            self.image = self.image_middle
        elif self.name in box_center:
            self.image_center = image.load(self.image_path_center)
            self.image = self.image_center

        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2 * gc.MARGIN, gc.IMAGE_SIZE - 2 * gc.MARGIN))

        #images border in correct position (rotation)
        if self.name in box_border and self.first_time == True:
            if self.name != '5.png' and self.name != '52.png':
                if self.row == 0:
                    self.image = transform.rotate(self.image, 180)
                elif self.row == 4:
                    self.image = transform.rotate(self.image, 0)
                elif self.col == 0:
                    self.image = transform.rotate(self.image, 270)
                elif self.col == 4:
                    self.image = transform.rotate(self.image, 90)

        if self.name in box_center:
            rotation_mode_center = [0, 90, 180, 270]
            self.image = transform.rotate(self.image, rotation_mode_center[random.randrange(0, 4)])
    def row(self, r): 
         self._row = r 

    def col(self, c): 
         self._col = c 

    def first_time(self, f): 
         self._first_time = f 

    def image(self, i): 
         self._image = i 
    
    def image(self): 
         return self._image
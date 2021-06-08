import random
import os
import game_config as gc

from pygame import image, transform

box_border = [a for a in gc.ASSET_FILES_BORDER]
box_middle = [a for a in gc.ASSET_FILES_MIDDLE]
box_center = [a for a in gc.ASSET_FILES_CENTER]

def available_boxes():
    box_counts = []
    box_counts.append(box_border)
    box_counts.append(box_middle)
    box_counts.append(box_center)
    print(random.choice(box_counts)[0])

    return box_counts

class Box:
    def __init__(self, index):

        self.index = index
        self.name = random.choice(available_boxes())[0]
        
        self.image_path_border = os.path.join(gc.ASSET_DIR_BORDER, self.name)
        self.image_path_middle = os.path.join(gc.ASSET_DIR_MIDDLE, self.name)
        self.image_path_center = os.path.join(gc.ASSET_DIR_CENTER, self.name)
        self.row = index // gc.NUM_TILES_SIDE
        self.col = index % gc.NUM_TILES_SIDE
        self.skip = False
        
        if (self.name in box_border):
            self.image_border = image.load(self.image_path_border)
            self.image = self.image_border
        elif (self.name in box_middle):
            self.image_middle = image.load(self.image_path_middle)
            self.image = self.image_middle
        else:
            self.image_center = image.load(self.image_path_center)
            self.image = self.image_center

        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2 * gc.MARGIN, gc.IMAGE_SIZE - 2 * gc.MARGIN))


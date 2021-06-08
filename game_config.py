import os

IMAGE_SIZE = 122
MARGIN = 6

NUM_TILES_BORDER = 11
NUM_TILES_MIDDLE = 5
NUM_TILES_CENTER = 1

NUM_TILES_SIDE = 5
NUM_TILES_TOTAL = 25


ASSET_DIR_BORDER = 'assets\\border'
ASSET_DIR_MIDDLE = 'assets\\middle'
ASSET_DIR_CENTER = 'assets\\center'

ASSET_FILES_BORDER = [x for x in os.listdir(ASSET_DIR_BORDER) if x[-3:].lower() == 'png']
ASSET_FILES_MIDDLE = [x for x in os.listdir(ASSET_DIR_MIDDLE) if x[-3:].lower() == 'png']
ASSET_FILES_CENTER = [x for x in os.listdir(ASSET_DIR_CENTER) if x[-3:].lower() == 'png']

assert len(ASSET_FILES_BORDER) == 11
assert len(ASSET_FILES_MIDDLE) == 5
assert len(ASSET_FILES_CENTER) == 1



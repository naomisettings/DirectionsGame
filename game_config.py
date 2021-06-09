import os

IMAGE_SIZE = 122
MARGIN = 6

NUM_TILES_BORDER = 14
NUM_TILES_MIDDLE = 8
NUM_TILES_CENTER = 1

NUM_TILES_SIDE = 5
NUM_TILES_TOTAL = 25

PIECE_SIZE = 222
MARGIN_PIECE = 8


ASSET_DIR_BORDER = 'assets\\border'
ASSET_DIR_MIDDLE = 'assets\\middle'
ASSET_DIR_CENTER = 'assets\\center'
ASSET_DIR_START_END = 'assets\\start_end'

ASSET_DIR_PIECE = 'assets\\piece'

ASSET_FILES_BORDER = [x for x in os.listdir(ASSET_DIR_BORDER)]
ASSET_FILES_MIDDLE = [x for x in os.listdir(ASSET_DIR_MIDDLE)]
ASSET_FILES_CENTER = [x for x in os.listdir(ASSET_DIR_CENTER)]
ASSET_FILES_START_END = [x for x in os.listdir(ASSET_DIR_START_END)]

ASSET_FILES_PIECE = [x for x in os.listdir(ASSET_DIR_PIECE)]

assert len(ASSET_FILES_BORDER) == 14
assert len(ASSET_FILES_MIDDLE) == 8
assert len(ASSET_FILES_CENTER) == 1
assert len(ASSET_FILES_START_END) == 2
assert len(ASSET_FILES_PIECE) == 1



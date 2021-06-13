import os
import game_config as gc

from pygame import image, transform

piece = gc.ASSET_DIR_PIECE
print(piece)

class Piece(object):

    def __init__(self, row, col):

        self.row = row
        self.col = col

        self.name = 'piece.png'
        self.image_path_piece = os.path.join(gc.ASSET_DIR_PIECE, self.name)
        self.image_piece = image.load(self.image_path_piece)
        self.image = self.image_piece

        self.image = transform.scale(self.image, (gc.PIECE_SIZE_HEIGH - 1 * gc.MARGIN_PIECE, gc.PIECE_SIZE_WITH - 2 * gc.MARGIN_PIECE))



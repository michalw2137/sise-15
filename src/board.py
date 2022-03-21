import numpy as np

SIZE = 4


class Board(object):

    def __init__(self, board):
        self.tiles = board
        self.print()

    def set_board(self, board):
        self.tiles = board

    def print(self):
        for i in range(SIZE):
            for ii in range(SIZE):
                print(self.tiles[i * SIZE + ii], end='\t')
            print()
        print()

    def move_tile(self, tile_id):  # TODO: fix this mess xd
        try:
            self.move_up(tile_id)
            return
        except IndexError:
            pass
        except ValueError:
            pass

        try:
            self.move_down(tile_id)
            return
        except IndexError:
            pass
        except ValueError:
            pass

        try:
            self.move_left(tile_id)
            return
        except IndexError:
            pass
        except ValueError:
            pass

        try:
            self.move_right(tile_id)
            return
        except IndexError:
            print("nie wykonano ruchu")
        except ValueError:
            print("nie wykonano ruchu")

    def move_up(self, tile_id):
        if tile_id < SIZE:
            raise IndexError(tile_id, 'move_up')

        if self.tiles[tile_id - SIZE] != 0:
            raise ValueError(tile_id, 'moving not empty tile')

        temp = self.tiles[tile_id]
        self.tiles[tile_id] = self.tiles[tile_id - SIZE]
        self.tiles[tile_id - SIZE] = temp

    def move_down(self, tile_id):
        if tile_id >= SIZE * (SIZE - 1):
            raise IndexError(tile_id, 'move_down')

        if self.tiles[tile_id + SIZE] != 0:
            raise ValueError(tile_id, 'moving not empty tile')

        temp = self.tiles[tile_id]
        self.tiles[tile_id] = self.tiles[tile_id + SIZE]
        self.tiles[tile_id + SIZE] = temp

    def move_left(self, tile_id):
        if tile_id % SIZE == 0:
            raise IndexError(tile_id, 'move_left')

        if self.tiles[tile_id - 1] != 0:
            raise ValueError(tile_id, 'moving not empty tile')

        temp = self.tiles[tile_id]
        self.tiles[tile_id] = self.tiles[tile_id - 1]
        self.tiles[tile_id - 1] = temp

    def move_right(self, tile_id):
        if (tile_id + 1) % SIZE == 0:
            raise IndexError(tile_id, 'move_right')

        if self.tiles[tile_id + 1] != 0:
            raise ValueError(tile_id, 'moving not empty tile')

        temp = self.tiles[tile_id]
        self.tiles[tile_id] = self.tiles[tile_id + 1]
        self.tiles[tile_id + 1] = temp

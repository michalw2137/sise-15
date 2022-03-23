import numpy as np

SIZE = 4


class Board(object):

    def __init__(self, board):
        self.tiles = []
        self.tiles = board
        self.blank_pos = self.tiles.index(0)
        self.print()

    def set_board(self, board):
        self.tiles = board

    def print(self):
        for i in range(SIZE):
            for ii in range(SIZE):
                print(self.tiles[i * SIZE + ii], end='\t')
            print()
        print()

    def find_legal_moves(self):
        moves = []
        print(f"1 try: BLAN POSITION = {self.blank_pos}")
        try:
            self.move_right(self.blank_pos - 1)
            moves.append(self.blank_pos - 1)
            print(f"{self.blank_pos - 1}, move_right")

        except (IndexError, ValueError) as e:
            print(e.args)

        print(f"2 try: BLAN POSITION = {self.blank_pos}")
        try:
            self.move_left(self.blank_pos + 1)
            moves.append(self.blank_pos + 1)
            print(f"{self.blank_pos + 1}, move_left")

        except (IndexError, ValueError) as e:
            print(e.args)

        print(f"3 try: BLAN POSITION = {self.blank_pos}")
        try:
            self.move_down(self.blank_pos - SIZE)
            moves.append(self.blank_pos - SIZE)
            print(f"{self.blank_pos - SIZE}, move_down")
        except (IndexError, ValueError) as e:
            print(e.args)

        print(f"4 try: BLAN POSITION = {self.blank_pos}")
        try:
            self.move_up(self.blank_pos + SIZE)
            moves.append(self.blank_pos + SIZE)
            print(f"{self.blank_pos + SIZE}, move_up")

        except (IndexError, ValueError) as e:
            print(e.args)

        return moves.sort()

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
        if tile_id < 0 or tile_id > SIZE * SIZE:
            raise IndexError(tile_id, 'move_up')

        if tile_id < SIZE:
            raise IndexError(tile_id, 'move_up')

        if self.tiles[tile_id - SIZE] != 0:
            raise ValueError(tile_id, 'moving not empty tile')

        temp = self.tiles[tile_id]
        self.tiles[tile_id] = self.tiles[tile_id - SIZE]
        self.tiles[tile_id - SIZE] = temp
        self.blank_pos += SIZE

    def move_down(self, tile_id):
        if tile_id < 0 or tile_id > SIZE * SIZE:
            raise IndexError(tile_id, 'move_down')

        if tile_id >= SIZE * (SIZE - 1):
            raise IndexError(tile_id, 'move_down')

        if self.tiles[tile_id + SIZE] != 0:
            raise ValueError(tile_id, 'moving not empty tile')

        temp = self.tiles[tile_id]
        self.tiles[tile_id] = self.tiles[tile_id + SIZE]
        self.tiles[tile_id + SIZE] = temp
        self.blank_pos -= SIZE

    def move_left(self, tile_id):
        if tile_id < 0 or tile_id > SIZE * SIZE:
            raise IndexError(tile_id, 'move_left')

        if tile_id % SIZE == 0:
            raise IndexError(tile_id, 'move_left')

        if self.tiles[tile_id - 1] != 0:
            raise ValueError(tile_id, 'moving not empty tile')

        temp = self.tiles[tile_id]
        self.tiles[tile_id] = self.tiles[tile_id - 1]
        self.tiles[tile_id - 1] = temp

        self.blank_pos += 1

    def move_right(self, tile_id):
        if tile_id < 0 or tile_id > SIZE*SIZE:
            raise IndexError(tile_id, 'move_right')

        if (tile_id + 1) % SIZE == 0:
            raise IndexError(tile_id, 'move_right')

        if self.tiles[tile_id + 1] != 0:
            raise ValueError(tile_id, 'moving not empty tile')

        temp = self.tiles[tile_id]
        self.tiles[tile_id] = self.tiles[tile_id + 1]
        self.tiles[tile_id + 1] = temp

        self.blank_pos -= 1

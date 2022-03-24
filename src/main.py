import time
from random import choice

from src.board import Board


def is_solved(board):
    return board.tiles == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]


if __name__ == '__main__':
    board = Board([4, 15, 7, 13, 12, 2, 11, 5, 1, 6, 8, 14, 9, 3, 10, 0])
    # board = Board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    start = time.time()
    moves = []

    while not is_solved(board):
        move = board.find_best_move()
        # print(board.find_legal_moves(), end='\t\t')
        # print(move)
        board.move_tile(move)
        moves.append(move)
        board.print()

    print(f"ruchy: {moves}")
    board.print()
    print(time.time() - start)

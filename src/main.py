from random import choice

from src.board import Board


def is_solved(board):
    return board.tiles == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]


if __name__ == '__main__':
    board = Board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    moves = []

    while not is_solved(board):
        move = choice(board.find_legal_moves())

        board.move_tile(move)
        moves.append(move)

    print(moves)
    print(f"ilosc ruchow = {len(moves)}")
    board.print()

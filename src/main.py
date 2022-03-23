from src.board import Board


def is_solved(board):
    return board == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


if __name__ == '__main__':
    board = Board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    while True:
        board.move_tile(int(input("Ktore pole chcesz ruszyc?: ")))
        board.print()


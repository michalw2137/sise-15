import unittest
from unittest import TestCase

from src.board import Board
from src.main import is_solved


class TestStringMethods(unittest.TestCase):

    def test_move_up(self):
        board = Board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(board.tiles, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

        board.move_up(4)
        self.assertEqual(board.tiles, [4, 1, 2, 3, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

        for i in range(4):
            with self.assertRaises(IndexError):
                board.move_up(i)

        for i in range(12, 16):
            board = Board([0, 0, 0, 0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
            with self.assertRaises(ValueError):
                board.move_up(i)

    def test_move_down(self):
        board = Board([4, 1, 2, 3, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(board.tiles, [4, 1, 2, 3, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

        board.move_down(0)
        self.assertEqual(board.tiles, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

        for i in range(12, 16):
            with self.assertRaises(IndexError):
                board.move_down(i)

        for i in range(8, 12):
            with self.assertRaises(ValueError):
                board.move_down(i)

    def test_move_left(self):
        board = Board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(board.tiles, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

        board.move_left(1)
        self.assertEqual(board.tiles, [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

        for i in (0, 4, 8, 12):
            with self.assertRaises(IndexError):
                board.move_left(i)

        for i in (3, 7, 11, 15):
            with self.assertRaises(ValueError):
                board.move_left(i)

    def test_move_right(self):
        board = Board([1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(board.tiles, [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

        board.move_right(0)
        self.assertEqual(board.tiles, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

        for i in (3, 7, 11, 15):
            with self.assertRaises(IndexError):
                board.move_right(i)

        for i in (1, 5, 9, 13):
            with self.assertRaises(ValueError):
                board.move_right(i)



if __name__ == '__main__':
    unittest.main()

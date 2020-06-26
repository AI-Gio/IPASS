import unittest
import SudokuSolver as ss

class MyTestCase(unittest.TestCase):

    # empty_cell
    def test_empty_cell(self):
        """
        Tests if function can find the first empty cell in the sudoku array
        """
        sudoku = [[0, 9, 0, 0, 0, 0, 2, 0, 0],
                  [4, 0, 0, 0, 5, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0],
                  [1, 0, 5, 0, 0, 0, 0, 0, 6],
                  [0, 0, 0, 3, 0, 2, 7, 0, 0],
                  [8, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 3, 0, 7, 0, 0, 0, 0, 0],
                  [6, 0, 0, 0, 0, 0, 0, 5, 0],
                  [0, 0, 0, 9, 0, 0, 0, 0, 0]]
        self.assertEqual(ss.SudokuSolver.empty_cell(sudoku), (0,0))

    def test_no_empty_cell(self):
        """
        Tests if function returns False if there is no empty cell
        """
        sudoku1 = [[5, 9, 6, 8, 7, 3, 2, 4, 1],
                   [4, 1, 7, 2, 5, 9, 6, 8, 3],
                   [3, 8, 2, 6, 1, 4, 5, 7, 9],
                   [1, 2, 5, 4, 9, 7, 8, 3, 6],
                   [9, 6, 4, 3, 8, 2, 7, 1, 5],
                   [8, 7, 3, 5, 6, 1, 4, 9, 2],
                   [2, 3, 1, 7, 4, 5, 9, 6, 8],
                   [6, 4, 9, 1, 2, 8, 3, 5, 7],
                   [7, 5, 8, 9, 3, 6, 1, 2, 4]]
        self.assertFalse(ss.SudokuSolver.empty_cell(sudoku1))

    # tests valid_number
    def valid_number(self):
        """

        """

        sudoku2 = [[0, 9, 0, 0, 0, 0, 2, 0, 0],
                   [4, 0, 0, 0, 5, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0],
                   [1, 0, 5, 0, 0, 0, 0, 0, 6],
                   [0, 0, 0, 3, 0, 2, 7, 0, 0],
                   [8, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 3, 0, 7, 0, 0, 0, 0, 0],
                   [6, 0, 0, 0, 0, 0, 0, 5, 0],
                   [0, 0, 0, 9, 0, 0, 0, 0, 0]]
        # row check
        self.assertFalse(ss.SudokuSolver.valid_number(sudoku2, 9, (0,0)))
        # box check
        self.assertFalse(ss.SudokuSolver.valid_number(sudoku2, 1, (3,0)))
        # column check
        self.assertFalse(ss.SudokuSolver.valid_number(sudoku2, 6 , (8,0)))
        # valid input number check
        self.assertTrue(ss.SudokuSolver.valid_number(sudoku2, 8, (4,4)))

    def test_smallest_str(self):
        coords = {(1,0):'123',
                  (2,0):'12345',
                  (3,0):'12'}
        self.assertEqual(ss.SudokuSolver.smallest_str(coords), ((3,0),'12'))

    def test_cell_possibilities(self):
        sudoku3 = [[5, 0, 6, 8, 7, 3, 2, 4, 1],
                   [4, 1, 7, 2, 5, 9, 6, 8, 3],
                   [3, 8, 2, 6, 1, 4, 5, 7, 9],
                   [1, 2, 5, 4, 9, 7, 8, 3, 6],
                   [9, 6, 4, 3, 8, 2, 7, 1, 5],
                   [8, 7, 3, 5, 6, 1, 4, 0, 2],
                   [2, 3, 1, 7, 4, 5, 9, 6, 8],
                   [6, 4, 9, 1, 2, 8, 3, 5, 7],
                   [7, 5, 8, 9, 3, 6, 1, 2, 4]]
        self.assertEqual(ss.SudokuSolver.cell_possibilities(sudoku3), {(1,0):'9', (7,5):'9'})

    def test_solve_sudoku(self):
        sudoNotSolved = [[0, 0, 4, 3, 0, 0, 2, 0, 9],
                         [0, 0, 5, 0, 0, 9, 0, 0, 1],
                         [0, 7, 0, 0, 6, 0, 0, 4, 3],
                         [0, 0, 6, 0, 0, 2, 0, 8, 7],
                         [1, 9, 0, 0, 0, 7, 4, 0, 0],
                         [0, 5, 0, 0, 8, 3, 0, 0, 0],
                         [6, 0, 0, 0, 0, 0, 1, 0, 5],
                         [0, 0, 3, 5, 0, 8, 6, 9, 0],
                         [0, 4, 2, 9, 1, 0, 3, 0, 0]]
        sudoSolved = [[8, 6, 4, 3, 7, 1, 2, 5, 9],
                      [3, 2, 5, 8, 4, 9, 7, 6, 1],
                      [9, 7, 1, 2, 6, 5, 8, 4, 3],
                      [4, 3, 6, 1, 9, 2, 5, 8, 7],
                      [1, 9, 8, 6, 5, 7, 4, 3, 2],
                      [2, 5, 7, 4, 8, 3, 9, 1, 6],
                      [6, 8, 9, 7, 3, 4, 1, 2, 5],
                      [7, 1, 3, 5, 2, 8, 6, 9, 4],
                      [5, 4, 2, 9, 1, 6, 3, 7, 8]]
        ss.SudokuSolver.solve_sudoku(sudoNotSolved)
        self.assertEqual(sudoNotSolved, sudoSolved)

    def test_str2array(self):
        sudoku7 = [[0, 4, 0, 1, 0, 0, 0, 5, 0],
                    [1, 0, 7, 0, 0, 3, 9, 6, 0],
                    [5, 2, 0, 0, 0, 8, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 7],
                    [0, 0, 0, 9, 0, 6, 8, 0, 0],
                    [8, 0, 3, 0, 5, 0, 6, 2, 0],
                    [0, 9, 0, 0, 6, 0, 5, 4, 3],
                    [6, 0, 0, 0, 8, 0, 7, 0, 0],
                    [2, 5, 0, 0, 9, 7, 1, 0, 0]]
        self.assertEqual(ss.SudokuSolver.str2array('040100050107003960520008000000000017000906800803050620090060543600080700250097100'), sudoku7)

        # This sudoku string isn't 81 chars long
        self.assertRaises(ValueError, ss.SudokuSolver.str2array, sudo_str='0401000501070039605200080000000000170009068008030506200900605436000807002500971')

        # This sudoku string contains a non valid character
        self.assertRaises(ValueError, ss.SudokuSolver.str2array, sudo_str='0401000501070039605200080000000000170009068008030506200900605436000807002500weird')

    def test_array2str(self):
        sudoku5 =    [[8, 6, 4, 3, 7, 1, 2, 5, 9],
                      [3, 2, 5, 8, 4, 9, 7, 6, 1],
                      [9, 7, 1, 2, 6, 5, 8, 4, 3],
                      [4, 3, 6, 1, 9, 2, 5, 8, 7],
                      [1, 9, 8, 6, 5, 7, 4, 3, 2],
                      [2, 5, 7, 4, 8, 3, 9, 1, 6],
                      [6, 8, 9, 7, 3, 4, 1, 2, 5],
                      [7, 1, 3, 5, 2, 8, 6, 9, 4],
                      [5, 4, 2, 9, 1, 6, 3, 7, 8]]
        self.assertEqual(ss.SudokuSolver.array2str(sudoku5), '864371259325849761971265843436192587198657432257483916689734125713528694542916378')
        # This sudoku misses one row
        sudoku6 =    [[8, 6, 4, 3, 7, 1, 2, 5, 9],
                      [3, 2, 5, 8, 4, 9, 7, 6, 1],
                      [9, 7, 1, 2, 6, 5, 8, 4, 3],
                      [4, 3, 6, 1, 9, 2, 5, 8, 7],
                      [1, 9, 8, 6, 5, 7, 4, 3, 2],
                      [2, 5, 7, 4, 8, 3, 9, 1, 6],
                      [6, 8, 9, 7, 3, 4, 1, 2, 5],
                      [7, 1, 3, 5, 2, 8, 6, 9, 4]]
        self.assertRaises(ValueError, ss.SudokuSolver.array2str, sudo_array=sudoku6)

        # This sudoku has a row that isn't 9 items long
        sudoku7 =    [[8, 6, 4, 3, 7, 1, 2, 5, 9],
                      [3, 2, 5, 8, 4, 9, 7, 6, 1],
                      [9, 7, 1, 2, 6, 5, 8, 4, 3],
                      [4, 3, 6, 1, 9, 2, 5, 8, 7],
                      [1, 9, 8, 6, 5, 7, 4, 3],
                      [2, 5, 7, 4, 8, 3, 9, 1, 6],
                      [6, 8, 9, 7, 3, 4, 1, 2, 5],
                      [7, 1, 3, 5, 2, 8, 6, 9, 4],
                      [5, 4, 2, 9, 1, 6, 3, 7, 8]]
        self.assertRaises(ValueError, ss.SudokuSolver.array2str, sudo_array=sudoku7)

        # This sudoku contains an non valid character
        sudoku8 =    [[8, 6, 4, 3, 7, 1, 2, 5, 9],
                      [3, 2, 5, 8, 4, 9, 7, 6, 1],
                      [9, 7, 1, 't', 6, 5, 8, 4, 3],
                      [4, 3, 6, 1, 9, 2, 5, 8, 7],
                      [1, 9, 8, 6, 5, 7, 4, 3, 2],
                      [2, 5, 7, 4, 8, 3, 9, 1, 6],
                      [6, 8, 9, 7, 3, 4, 1, 2, 5],
                      [7, 1, 3, 5, 2, 8, 6, 9, 4],
                      [5, 4, 2, 9, 1, 6, 3, 7, 8]]
        self.assertRaises(ValueError, ss.SudokuSolver.array2str, sudo_array=sudoku8)

if __name__ == '__main__':
    unittest.main()

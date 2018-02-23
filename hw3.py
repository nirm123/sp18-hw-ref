# -*- coding: utf-8 -*-
# CS 196 SP18 HW3

# is unique
def is_unique(word):
    """
    Given a string, returns true if the string's characters are unique.
    This is case-INsensitive. This function should treat 'a' and 'A' as the same character.

    Args:
        (str) word: the input string, not necessarily a word

    Returns:
        (bool) True if the string's characters are unique, False otherwise.
    """
    pass

def is_anagram(w1, w2):
    """
    Given two strings, returns if they are anagrams of each other.
    This function is case-SENSITIVE.
    
    Args:
        (str) w1: an input string
        (str) w2: another input string
    
    Returns:
        (bool) whether or not the strings are anagrams
    """

# Tic-Tac-Toe (n x n)
def tic_tac_toe(arr):
    """
    Given a square array, returns the winner of Tic-Tac-Toe
    A person has won Tic-Tac-Toe if:
        - They have all spaces in a row
        - They have all spaces in a column
        - They have all spaces in a diagonal

    Example Array (no brackets for clarity)

    X O X X
    - X O O
    - - X X
    - - O X

    In this example, X wins (returns 2).

    Args:
        [[str]] arr: a valid square (n x n) array
    Returns:
        (int)
        0 if there is no winner
        1 if 0 is the winner
        2 if X is the winner
    """
    pass

def matrix_transpose(matrix):
    """
    Write a function that, given a 2d array (matrix) returns the trasnpose
    of that matrix. The transpose of a matrix is when the rows of the
    source matrix become the columns of the resulting matrix:

    1  2      1  3  5
    3  4  ->  2  4  6
    5  6

    It may be useful to read this Wikipedia article on matrix transposes:
    https://en.wikipedia.org/wiki/Transpose

    Note: You may not use any builtin functions in this problem.

    Example(s)
    ----------
    Example 1:
    Input: [[1,2],[3,4],[5,6]]
    Output:
    [[1, 3, 5], [2, 4, 6]]

    Example 2:
    Input:
        [['a','b','c','d'],
         ['e','f','g','h'],
         ['i','j','k','l'],
         ['m','n','o','p']]
    Output:
        [['a','e','i','m'],
         ['b','f','j','n'],
         ['c','g','k','o'],
         ['d','h','l','p']]

    Args:
        [[object]] matrix: a 2d array of arbitrary rectangular size with arbitrary data elements

    Returns:
        [[object]] transposed matrix as a 2d array
    """
    pass

# minesweeper problem
def initialize_counts(minefield):
    """
    Minesweeper is a popular (once-popular?) puzzle game where the player's
    goal is to find and label a set of mines in a minefield. The "minefield"
    is a rectangular grid of tiles -- each tile contains either a mine or a
    number representing the number of neighboring tiles that contain a mine.
    The tiles' contents are initially hidden from the player. The player can
    reveal a tile’s contents, but must be careful not to reveal a mine
    (revealing a mine ends the game). When the player reveals a mine-free tile,
    that tile’s mine-free neighbors are also revealed, recursively. The
    player’s task is to reveal all of the mine-free tiles without revealing a
    tile that contains a mine.

    For this problem, you are given a minefield whose mine-free tiles do not
    yet contain the count of neighboring tiles that contain mines. Your task
    is to initialize these counts.

    Specifically, you are given a 2-dimensional n * m integer array (‘minefield’)
    representing the minefield. If a tile (x,y) contains a mine, then
    minefield[x][y] contains -1. Tiles that do not contain a mine currently
    contain 0.

    For example, suppose you are given a 3 * 4 minefield with two mines, one
    at (0,2) and the other at (1, 0). minefield would look like this:

    minefield = [[ 0, 0, -1, 0],
                 [-1, 0,  0, 0],
                 [ 0, 0,  0, 0] ]

    You can see that the counts for the mine-free tiles are not yet calculated.
    Recall that each mine-free tile should contain the number of neighboring
    tiles that contain a mine. Neighbors include diagonals; for example, the
    neighbors of tile (0, 0) are (0, 1), (1, 0), and (1, 1).

    For the above example, here’s what minefield should look like when
    initialize_counts returns:

    [[ 1, 2, -1, 1],
     [-1, 2,  1, 1],
     [ 1, 1,  0, 0] ]

    Notes:
        * Do not return a new array -- update the one passed in as an argument
        * Do not change the mines. In other words, if an index contains -1
        before initialize_counts runs, it should contain -1 after
        initialize_counts runs

    Args:
        (List[List[int]]) minefield: 2D array representing the minefield

    Returns:
        (None) This method doesn't return anything; it updates the argument instead
    """
    pass

import pytest

"""
If we scan through the original array, we observe that the 2D pattern begins at the second row and the third column
OverflowErrorthe larger grid (the  in the second row and third column of the larger grid is the top-left corner of the pattern we are searching for).

So, a 2D pattern of  digits is said to be present in a larger grid , if the latter contains a contiguous, rectangular
2D grid of digits matching with the pattern , similar to the example shown above.
"""

@pytest.mark.parametrize(
    'grid, pattern', [
        (
            [
                [7, 2, 8, 3, 4, 5, 5, 8, 6, 4],
                [6, 7, 3, 1, 1, 5, 8, 6, 1, 9],
                [8, 9, 8, 8, 2, 4, 2, 6, 4, 3],
                [3, 8, 3, 0, 5, 8, 9, 3, 2, 4],
                [2, 2, 2, 9, 5, 0, 5, 8, 1, 3],
                [5, 6, 3, 3, 8, 4, 5, 3, 7, 4],
                [6, 4, 7, 3, 5, 3, 0, 2, 9, 3],
                [7, 0, 5, 3, 1, 0, 6, 6, 0, 1],
                [0, 8, 3, 4, 2, 8, 2, 9, 5, 6],
                [4, 6, 0, 7, 9, 2, 4, 1, 3, 7],
            ], [
                [9, 5, 0, 5],
                [3, 8, 4, 5],
                [3, 5, 3, 0],
            ]
        ), (
            [
                [1, 1],
                [1, 1],
            ],
            [
                [1, 1],
                [1, 1],
            ]
        )
    ])
def test_positive_case(grid, pattern):
    assert find_pattern(grid, pattern)


def test_negative_case():
    input_grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]

    pattern_to_find = [
        [2, 2],
        [2, 2],
    ]

    assert not find_pattern(input_grid, pattern_to_find)


def find_pattern(grid, pattern):
    grid_height, grid_width = len(grid), len(grid[0])
    pattern_height, pattern_width = len(pattern), len(pattern[0])

    def find_pattern_starting_from(grid_i, grid_j):
        for k in range(pattern_height):
            for m in range(pattern_width):
                if grid[i + k][j + m] != pattern[k][m]:
                    return False
        return True

    for i in range(grid_height - pattern_height + 1):
        for j in range(grid_width - pattern_width + 1):
            if find_pattern_starting_from(i, j):
                return True

    return False

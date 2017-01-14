import numpy as np


"""
You are given a 2D matrix, a, of dimension MxN and a positive integer R. You have to rotate the matrix R times and print
the resultant matrix. Rotation should be in anti-clockwise direction.

Rotation of a 4x5 matrix is represented by the following figure. Note that in
one rotation, you have to shift elements by one step only (refer sample tests
for more clarity)."""

def rotate(arr, N, M, R):
    def coordinates(i, j):
        for p in range(j, M - j - 1):
            yield i, p

        for p in range(i, N - i - 1):
            yield p, M - j - 1

        for p in range(M - j - 1, j, -1):
            yield N - i - 1, p

        for p in range(N - i - 1, i, -1):
            yield p, j

    # No circles in the array
    if 2 * (N + M) - 4 == 0:
        return
    # If we rotate F = 2 * (ROWS - 1) + 2 * (COLS - 1) times we'll come back to initial position, no reason for rotating
    # more than that
    R = R % (2 * (N + M) - 4)

    number_of_circles = min(N, M) // 2
    for c in range(number_of_circles):
        coords = list(coordinates(c, c))

        for i in range(len(coords) - R):
            from_i, from_j = coords[i]
            to_i, to_j = coords[i + R]
            arr[from_i][from_j], arr[to_i][to_j] = arr[to_i][to_j], arr[from_i][from_j]


def test_dot_array_isnt_rotated():
    arr = [0]
    rotate(arr, 1, 1, 1)

    assert arr == [0]


def test_smallest_possible_array_is_correctly_rotated():
    arr = np.array([
        [1, 2],
        [3, 4],
    ])

    rotate(arr, *arr.shape, R=1)

    assert np.array_equiv(arr, [
        [2, 4],
        [1, 3],
    ])


def test_smallest_possible_array_returns_back_to_initial_state_after_certain_amount_of_rotations():
    arr = np.array([
        [1, 2],
        [3, 4],
    ])

    rotate(arr, *arr.shape, R=4)

    assert np.array_equiv(arr, [
        [1, 2],
        [3, 4],
    ])

def test_array_with_two_circles_is_rotated_correctly_after_first_rotation():
    arr = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])


    rotate(arr, *arr.shape, R=1)

    assert np.array_equiv(arr, np.array([
        [2, 3, 4, 8],
        [1, 7, 11, 12],
        [5, 6, 10, 16],
        [9, 13, 14, 15]
    ]))


if __name__ == '__main__':
    arr = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])

    ROWS, COLS = arr.shape
    R = 1

    print('Before rotation')
    print(arr)

    rotate(arr, ROWS, COLS, R)

    print('After rotation')
    print(arr)

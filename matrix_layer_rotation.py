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


    number_of_circles = min(N, M) // 2
    for c in range(muber_of_circles):
        coords = list(coordinates(c, c))

        for i in range(len(coords) - R):
            from_i, from_j = coords[i]
            to_i, to_j = coords[i + R]
            arr[from_i][from_j], arr[to_i][to_j] = arr[to_i][to_j], arr[from_i][from_j]


arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

ROWS, COLS = arr.shape
R = 1

# If we rotate F = 2 * (ROWS - 1) + 2 * (COLD - 1) times we'll come back to initial position, no reason for rotating
# more than that
R = R % (2 * (ROWS + COLS) - 4)

print('Before rotation')
print(arr)

rotate(arr, ROWS, COLS, R)

print('After rotation')
print(arr)

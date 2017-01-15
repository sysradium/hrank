"""
Given a size N draw the rangoli alphabet 

N = 3
----c---- 0      4
--c-b-c-- 1    2 4 6
c-b-a-b-c 2  0 2 4 6 8
--c-b-c-- 3    2 4 6
----c---- 4      4

N = 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

Width contains K = 2 * SIZE - 1 letters. -1 excludes double counting of the letter in the center
Each letter has a connection except for the rightmost one, this there are K - 1 of them
Thus the width of the grid is K + (K - 1) = 2 * K - 1 = 2 * (2 * SIZE - 1) - 1 = 4 * SIZE - 3
"""
SIZE = 10

heigth = 2 * SIZE - 1
width = 4 * SIZE - 3
center = (width - 1) // 2


def convert_to_letter(index):
    return chr(ord('a') + SIZE - index - 1)


def heaviside_func(x):
    return 0 if x < 0 else 1


for i in range(heigth):
    for j in range(width):
        char = '-'

        if j % 2 == 0:
            k = i - heaviside_func(i - SIZE) * (2 * i - center)

            if -k <= (j - center) / 2 <= k:
                char = convert_to_letter(abs(abs(j - center) // 2 - k))

        print(char, end='')

    print('')

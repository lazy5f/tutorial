"""
D: all possible moves

T: tiles
xr, xc: index of empty tile (None)
r: number of random moves for initial shuffle
"""

from random import choice


D = [(-1, 0), (1, 0), (0, -1), (0, 1)]


T, xr, xc = [[0, 1, 2], [3, 4, 5], [6, 7, None]], 2, 2
r = 5


# Shuffle initially.
for _ in range(r):
    while True:
        dr, dc = choice(D)
        xr1, xc1 = xr + dr, xc + dc
        if 0 <= xr1 < 3 and 0 <= xc1 < 3:
            break
    
    T[xr][xc], T[xr1][xc1], xr, xc = T[xr1][xc1], None, xr1, xc1


# Do moves until completed.
while T != [[0, 1, 2], [3, 4, 5], [6, 7, None]]:
    # Print tiles.
    for r in range(3):
        for c in range(3):
            print(' ' if r == xr and c == xc else T[r][c], end=' ')
        print()
    
    # Get tile for move.
    m = eval(input())
    
    # Find and move tile.
    for dr, dc in D:
        xr1, xc1 = xr + dr, xc + dc
        if 0 <= xr1 < 3 and 0 <= xc1 < 3 and T[xr1][xc1] is m:
            T[xr][xc], T[xr1][xc1], xr, xc = T[xr1][xc1], None, xr1, xc1
            break
    else:
        print('Incorrect')


print('Good!')
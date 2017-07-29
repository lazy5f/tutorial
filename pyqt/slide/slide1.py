"""
Slide puzzle using console

T[r][c]: tiles at row r and column c
xr, xc: row and colume of empty tile (None)
r: number of random moves for initial shuffle
"""

from random import choice


# All possible moves
D = [(-1, 0), (1, 0), (0, -1), (0, 1)]


T, xr, xc = [[0, 1, 2], [3, 4, 5], [6, 7, None]], 2, 2
r = 5


# Shuffle initially.
for _ in range(r):
    # Select randomly a tile at (tr, tc) to move, 
    while True:
        dr, dc = choice(D)
        tr, tc = xr + dr, xc + dc
        if 0 <= tr < 3 and 0 <= tc < 3:
            break
    
    # Move a tile at (tr, tc) to (xr, xc).
    T[xr][xc], T[tr][tc], xr, xc = T[tr][tc], None, tr, tc


# Do moves until completed.
while T != [[0, 1, 2], [3, 4, 5], [6, 7, None]]:
    # Print tiles.
    for r in range(3):
        print(' '.join(' ' if T[r][c] is None else str(T[r][c]) for c in range(3)))
    
    # Get tile for move.
    m = eval(input('Tile number to move? '))
    
    # Find input tile at (tr, tc) and move it to (xr, tc).
    for dr, dc in D:
        tr, tc = xr + dr, xc + dc
        if 0 <= tr < 3 and 0 <= tc < 3 and T[tr][tc] is m:
            T[xr][xc], T[tr][tc], xr, xc = T[tr][tc], None, tr, tc
            break
    else:
        print('Invalid input')


print('Good!')

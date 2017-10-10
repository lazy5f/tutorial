"""
All digits enumeration solution to https://www.acmicpc.net/problem/1107

z: number of minimum pushes
"""

# Input
N, M = eval(input()), eval(input())
B1 = input() if M > 0 else ''

# B: sorted list of unbroken buttons
B = sorted(set(range(10)).difference(map(int, B1.split())))
nB = len(B)

# Using + and - only
z = abs(N - 100)

# Consider each number of possible digits
for d in range(len(str(500000))):
    # Enumerate unique number that represents each possible channel using B. 
    for x in range(nB**(d + 1)):
        # Get channel corresponding  to x.
        c = 0
        for p in range(d + 1):
            c += B[x % nB] * 10**p
            x //= nB
        
        # Check less.
        z = min(z, len(str(c)) + abs(N - c))

print(z)

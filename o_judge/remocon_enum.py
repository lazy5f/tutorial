"""
Recursive solution (considering small amount of possible channels) to
  https://www.acmicpc.net/problem/1107

z: number of minimum pushes
"""

# Input
N, M = eval(input()), eval(input())
B1 = input() if M > 0 else ''

# BB[b] is True iff b is broken.
B = [*map(int, B1.split())]
BB = [(b in B) for b in range(10)]

# Using + and - only
z = abs(N - 100)

# Using channel 0 if possible
if not BB[0]:
    z = min(z, 1 + N)

# Enumerate channel 1 to 999999.
for c in range(1, 1000000):
    # Check possible channel using unbroken buttons.
    c1 = c
    while c1 > 0:
        if BB[c1 % 10]:  # Broken button is needed.
            break
        c1 //= 10
    
    else:
        # Update if less pushes.
        z = min(z, len(str(c)) + abs(N - c))

print(z)

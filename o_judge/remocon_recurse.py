"""
Recursive solution (considering small amount of possible channels) to
  https://www.acmicpc.net/problem/1107

z: number of minium pushes
"""

# Input
N, M = eval(input()), eval(input())
B1 = input() if M > 0 else ''

# B: sorted list of unbroken buttons, Na: list of digits of N
B = sorted(set(range(10)).difference(map(int, B1.split())))
Na = [*map(int, reversed(str(N)))]


def min_push(c0, p):
    if p < 0:
        return len(str(c0))
    
    for k in range(len(B)):
        if B[k] >= Na[p]:
            break
    else:
        k += 1
    
    z0 = 500000
    
    if k > 0:
        c = c0 + B[k - 1] * 10**p + sum(B[-1] * 10**q for q in range(p))
        z0 = min(z0, len(str(c)) + N - c)
    
    if k < len(B) and B[k] == Na[p]:
        z0 = min(z0, min_push(c0 + Na[p] * 10**p, p - 1))
        k += 1
    
    if k < len(B) and B[k] > Na[p]:
        c = c0 + B[k] * 10**p + sum(B[0] * 10**q for q in range(p))
        z0 = min(z0, len(str(c)) + c - N)
    
    return z0


z = abs(N - 100)

if len(B) > 0:
    if len(B) == 1 and B[0] == 0:
        # Only button 0 is available.
        z = min(z, 1 + N)
    
    else:
        b0_plus = B[1] if B[0] == 0 else B[0]  # minimum button greater than 0
        c = b0_plus * 10**len(Na) + sum(B[0] * 10**q for q in range(len(Na)))
        z = min(z, len(str(c)) + c - N)
        
        if len(Na) > 1:
            c = sum(B[-1] * 10**q for q in range(len(Na) - 1))
            z = min(z, len(str(c)) + N - c)
        
        z = min(z, min_push(0, len(Na) - 1))

print(z)

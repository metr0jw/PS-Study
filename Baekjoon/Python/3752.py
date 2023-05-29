def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p:
            p += 1
        else:
            while n % p == 0:
                n //= p
            result -= result // p
    if n > 1:
        result -= result // n
    return result

def determinant(matrix, mul=1):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        total = 0
        for i in range(width):
            m = [[matrix[x][y] for y in range(width) if y != i] for x in range(1, width)]
            total += mul * determinant(m ,mul * matrix[0][i]) * (-1)**(i % 2)
        return total
    
def solve(S):
    n = len(S)
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = phi(gcd(S[i], S[j]))
    return determinant(matrix)

ans = []

T = int(input())
for _ in range(T):
    n = int(input())
    S = list(map(int, input().split()))

print(solve(S))

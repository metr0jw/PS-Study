import sys


input = sys.stdin.readline
print = sys.stdout.write

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b


def identity_matrix(K):
    I = [[0 for _ in range(K)] for _ in range(K)]
    for i in range(K):
        I[i][i] = 1
    return I

def matrix_mult(A, B):
    K = len(A)
    result = [[0 for _ in range(K)] for _ in range(K)]
    for i in range(K):
        for j in range(K):
            for k in range(K):
                result[i][j] += A[i][k] * B[k][j]
    return result

def matrix_power(matrix, n):
    if n == 0:
        return identity_matrix(len(matrix))
    elif n == 1:
        return matrix
    else:
        return matrix_mult(matrix, matrix_power(matrix, n-1))

def matrix_add(A, B):
    K = len(A)
    result = [[0 for _ in range(K)] for _ in range(K)]
    for i in range(K):
        for j in range(K):
            result[i][j] = A[i][j] + B[i][j]
    return result

def compute_S(K, M, N, a, d):
    S = [[0 for _ in range(K)] for _ in range(K)]
    for i in range(N+1):
        F = fibonacci(a + i * d)
        M_i = matrix_power(M, i)
        S = matrix_add(S, [[F * M_i[r][c] for c in range(K)] for r in range(K)])
    return S

user_input = input().split()

K, a, d, N = int(user_input[0]), int(user_input[1]), int(user_input[2]), int(user_input[3])
for i in range(K):
    user_input = input().split()
    for j in range(K):
        user_input[j] = int(user_input[j])
    if i == 0:
        M = [user_input]
    else:
        M.append(user_input)
    
S = compute_S(K, M, N, a, d)

for row in S:
    for col in row:
        print(str(col) + ' ')
    print('\n')

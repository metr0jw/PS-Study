from sys import stdin, stdout


n, k = map(int, stdin.readline().split())

n_fact = 1
k_fact = 1
n_sub_k = 1

if k < 0 or k > n:
    stdout.write(str(0))

elif k <= n:
    for i in range(1, n + 1):
        n_fact *= i
    for i in range(1, k + 1):
        k_fact *= i
    for i in range(1, n - k + 1):
        n_sub_k *= i
    
    stdout.write(str(int(n_fact/(k_fact * n_sub_k))))

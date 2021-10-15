import sys


def eratos(m, n, prime=None):
    if prime:
        for i in range(m, n+1, m):
            if i != m:
                prime[i] = 0
        return prime

    prime_num = []
    num_list = [1] * (n+1)
    num_list[0] = 0
    num_list[1] = 0

    for i in range(2, n+1):
        if num_list[i] == 1:
            num_list = eratos(i, n, num_list)

    for i in range(m):
        num_list[i] = 0
    for i in range(2, n+1):
        if num_list[i] == 1:
            prime_num.append(i)
    return prime_num

m, n = map(int, input().split())

if n <= 1:
    quit()

prime_num = eratos(m, n)

for num in prime_num:
    print(num)

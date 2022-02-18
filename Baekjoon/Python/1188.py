def gcd(n ,m):
    if n % m == 0:
        return m

    return gcd(m, n % m)


n, m = map(int, input().split())
print(m - gcd(n, m))
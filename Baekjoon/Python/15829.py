L = int(input())
string = input()
res = 0

for i in range(L):
    res += (ord(string[i]) - 96) * (31 ** i)
print(res % 1234567891)

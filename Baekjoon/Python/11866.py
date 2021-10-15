user_input = input().split()
n = int(user_input[0])
k = int(user_input[1]) - 1
table = []
jose = []
for i in range(n):
    table.append(i+1)
    
location = 0
for i in range(n):
    table_len = len(table)
    for j in range(k):
        location += 1
    while location >= table_len:
        location -= table_len
    jose.append(table[location])
    table.remove(table[location])
print("<", end="")
for i in range(n):
    if i == n - 1:
        print(f"{jose[i]}>", end="")
        break
    print(f"{jose[i]}, ", end="")

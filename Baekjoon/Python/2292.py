n = int(input())

hex = 1 
cnt = 1
while n > hex :
    hex += 6 * cnt
    cnt += 1
print(cnt)
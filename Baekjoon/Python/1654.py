n, k = map(int, input().split())
max_len = []
len_of_lan = 0

for i in range(n):
    max_len.append(int(input()))
    len_of_lan += max_len[i]
max_len.sort()
len_of_lan //= k

start = 1
end = max(max_len)

while start <= end:
    sum_of_div = 0
    mid = (start + end) // 2
    for i in max_len:
        sum_of_div += i // mid

    if sum_of_div >= k:
        start = mid + 1
    elif sum_of_div < k:
        end = mid - 1

print(end)

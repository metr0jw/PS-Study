n = int(input())

cnt = 0
num_to_contain = 666
while True:
    if '666' in str(num_to_contain):
        cnt += 1
    if cnt == n:
        print(num_to_contain)
        break
    num_to_contain += 1

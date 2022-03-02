import sys


n = int(input())
people = [0 for _ in range(n)]
rank = []

for i in range(n):
    people[i] = list(map(int, input().split()))

for idx, person in enumerate(people):
    rank_num = 1
    for idx_cmp, person_cmp in enumerate(people):
        if idx == idx_cmp:
            continue
        weight_cmp = 0
        height_cmp = 0

        if person[0] < person_cmp[0]:
            weight_cmp = 1
        if person[1] < person_cmp[1]:
            height_cmp = 1

        if (weight_cmp and height_cmp) == 1:
            rank_num += 1
    rank.append(rank_num)

for r in rank:
    print(r, end=" ")

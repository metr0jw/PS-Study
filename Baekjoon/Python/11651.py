import sys

loc_list = []
for i in range(int(sys.stdin.readline())):
    loc_list.append(list(map(int, sys.stdin.readline().split())))

loc_list = sorted(loc_list, key=lambda x:(x[1], x[0]))
for loc in loc_list:
    sys.stdout.writelines(f'{loc[0]} {loc[1]}\n')

n = int(input())
user_list = []
for i in range(n):
    member_age, member_name = map(str, input().split(' '))
    member_age = int(member_age)
    user_list.append([member_age, member_name])

user_list = sorted(user_list, key=lambda x: x[0])
for user in user_list:
    print(f'{user[0]} {user[1]}')

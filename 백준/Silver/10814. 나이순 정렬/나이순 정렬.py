n = int(input())
member = []

for i in range(n):
    age, name = input().split()
    member.append([int(age), name])

# 각 회원을 나이 순으로 정렬
member.sort(key=lambda member: member[0])

for i in range(0, n):
    print(member[i][0], member[i][1])
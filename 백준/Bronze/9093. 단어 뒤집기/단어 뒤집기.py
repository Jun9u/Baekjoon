n = int(input())

for _  in range(n):
    str = list(input().split())
    for i in range(len(str)):
        str[i] = str[i][::-1]
    print(*str)

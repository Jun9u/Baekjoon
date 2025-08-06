charge = [500, 100, 50, 10, 5, 1]

n = int(input())
n = 1000 - n
cnt = 0

for c in charge:
    if n >= c:
        cnt += n//c
        n %= c
print(cnt)
N = int(input())
P = []

for _ in range(N):
    point = list(map(int, input().split()))
    P.append(point)
    
P.sort()
for i in range(N):
    print("%d %d" %(P[i][0], P[i][1]))
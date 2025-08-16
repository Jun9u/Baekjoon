N = int(input())
P = []

for _ in range(N):
    point = list(map(int, input().split()))
    P.append(point)

for i in range(N):
    P[i][0], P[i][1] = P[i][1], P[i][0]
    
P.sort()
for i in range(N):
    P[i][1], P[i][0] = P[i][0], P[i][1]
    print("%d %d" %(P[i][0], P[i][1]))
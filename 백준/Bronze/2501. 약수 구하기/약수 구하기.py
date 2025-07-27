n, k = map(int, input().split())

num=numi=0

for i in range(1, n+1):
    if n%i==0:
        num+=1
    if num==k:
        numi=i
        break
print(numi)
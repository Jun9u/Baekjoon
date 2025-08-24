k = int(input())
L = []
 
for _ in range(k):
    num = int(input())
    if num == 0:
        L.pop()
    else:
        L.append(num)
        
total = 0
for x in L:
    total += x
print(total)
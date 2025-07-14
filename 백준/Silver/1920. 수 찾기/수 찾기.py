n = int(input())
nums = set(map(int, input().split()))
m = int(input())
queries = map(int, input().split())

for q in queries:
    print(1 if q in nums else 0)
import sys

T = int(sys.stdin.readline().strip())

# A, B, C 버튼이 각각 300초, 60초, 10초
cntA = T // 300
T %= 300

cntB = T // 60
T %= 60

cntC = T // 10
T %= 10

if T != 0:
    print(-1)
else:
    print(cntA, cntB, cntC)

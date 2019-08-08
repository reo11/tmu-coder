import math
n = int(input())

x = [0] * n; y = [0] * n

def dis(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

for i in range(n):
    x[i], y[i] = map(int, input().split())

ans = 0

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        ans = max(ans, dis([x[i], y[i]], [x[j], y[j]]))

print(ans)


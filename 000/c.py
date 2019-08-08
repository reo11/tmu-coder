n, y = map(int, input().split())

ans = ["-1", "-1", "-1"]
for i in range(n+1):
    for j in range(n+1):
        if i + j > n:
            continue
        k = n - i - j
        if i * 10000 + j * 5000 + k * 1000 == y:
            ans = list(map(str, [i, j, k]))
            break
print(" ".join(ans))

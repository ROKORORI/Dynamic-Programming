import sys
input = sys.stdin.readline
# 1
n, k = map(int, input().rstrip().split())
# dp, weight, val
dp, w, v = [[0] * (k + 1) for i in range(n + 1)], [0] * (n + 1), [0] * (n + 1)
for i in range(1, n + 1):
    a, b = map(int, input().rstrip().split())
    w[i], v[i] = a, b
# 2
for i in range(1, n + 1):
    for j in range(1, k + 1):
        if w[i] <= k:  # 물품 weight < 배낭 weight
            #  직전 배낭 가치 vs 현재 무게를 뺀 dp에 저장된 무게의 배낭 가치 + 지금 가치 비교
            if j - w[i] >= 0:
                dp[i][j] = max(v[i] + dp[i - 1][j - w[i]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
        else:  # weight > k
            dp[i][j] = dp[i - 1][j]
print(dp[n][k])
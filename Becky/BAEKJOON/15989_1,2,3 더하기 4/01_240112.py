# https://www.acmicpc.net/problem/15989
# 12:30-13:19
dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]
for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(int(input())):
    n = int(input())
    print(dp[n])
    
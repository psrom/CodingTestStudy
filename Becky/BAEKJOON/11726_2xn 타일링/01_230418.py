# 문제: https://www.acmicpc.net/problem/11726
n = int(input())

result = [0] * 1001
result[1] = 1
result[2] = 2

for i in range(3, n+1):
    result[i] = (result[i-1]+result[i-2])%10007

print(result[n])

import sys
limit_number = 15000
input = sys.stdin.readline

N = int(input())

Ti = []
Pi = []
for _ in range(N):
    a, b = map(int, input().split())
    Ti.append(a)
    Pi.append(b)


answer = float("-inf")
memo = [0]*(N+1)


for i in range(N):
    answer = max(answer, memo[i])
    if i+Ti[i] <= N+1:
        memo[i+Ti[i]] = max(memo[i+Ti[i]], answer+Pi[i])

print(memo[-1])


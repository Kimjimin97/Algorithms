import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

distance = list(map(int, input().split()))
costs = list(map(int, input().split()))

d = sum(distance)


queue = deque()
min_Oil = float("Inf")
answer = 0

for i in range(len(distance)):
    min_Oil = min(min_Oil, costs[i])
    answer += min_Oil*distance[i]
print(answer)
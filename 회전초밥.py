from collections import deque
import sys
input= sys.stdin.readline
N,d,k,c = map(int, input().split())

menu = [0]*(d+1)

table = []
for _ in range(N):
    table.append(int(input()))

table += table[:N-1]


eat = deque()
cnt = 0
answer = float("-Inf")

for i, f in enumerate(table):
    menu[f] += 1
    eat.append(f)
    if menu[f] == 1:
        cnt += 1
    
    if i <k-1:
        continue

    if menu[c] == 0:
        answer = max(answer, cnt+1)
    else: 
        answer = max(answer, cnt)
    
    top = eat.popleft()
    menu[top] -= 1
    if menu[top] == 0:
        cnt -= 1

print(answer)
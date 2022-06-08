import sys
from itertools import combinations
input = sys.stdin.readline


N = int(input())

ok = list(map(int, input().split()))
graph =[]

for _ in range(N):
    graph.append(list(map(int, input().split())))



items = []
answer = float("Inf")
answer_li = []

for i in range(N+2):
    items += list(combinations([k for k in range(N)],i))


for item in items:
    now = [0]*5
    for it in item:
        for a in range(5):
            now[a] += graph[it][a]

    flag = True
    for b in range(4):
        if now[b] < ok[b]:
            flag = False
            break
    if flag:
        if answer > now[-1]:
            answer = now[-1]
            answer_li = [list(item)]
        elif answer == now[-1]:
            answer_li.append(list(item))

if answer == float("Inf"):
    print(-1)
else:
    print(answer)
    answer_li.sort()
    answers = []
    for an in answer_li[0]:
        answers.append(an+1)
    
    print(*answers)
    


import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
n, T = map(int, input().split())

input = sys.stdin.readline
graph = []
graph.append([0,0])
for _ in range(n):
    graph.append(list(map(int, input().split())))

graph.sort()

answer = float("Inf")

def dfs(L,n):
    global answer

    if L == len(graph):
        if graph[L][1] >= T :
            print(graph[L][1], n)
            answer = min(n, answer)
        return

    if graph[L][1] >= T:
        answer = min(n, answer)
        return
    
    if n > answer:
        return

    
    for i in range(L+1, len(graph)):
        if (abs(graph[i][0] - graph[L][0] ) <= 2 ) and (abs(graph[i][1] - graph[L][1] ) <= 2 ):
            dfs(i,n+1)
    

dfs(0,0)
if answer == float("inf"):
    print(-1)
else:
    print(answer)

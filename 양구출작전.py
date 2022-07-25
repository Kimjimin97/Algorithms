from email.mime import base
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())


wolf_graph = [0,0]
sheep_graph = [0,0]
graph = [[] for _ in range(N+1)]


for k in range(N-1):
    a,b,c = map(str, input().split())
    b,c = int(b), int(c)
    if a == "S":
        sheep_graph.append(b)
        wolf_graph.append(0)
    else:
        sheep_graph.append(0)
        wolf_graph.append(b)
    graph[c].append(k+2)

    
def dfs(v):
    sheep = 0
    for k in graph[v]:
        sheep += dfs(k)
    if wolf_graph[v] > 0 : ## 늑대가 있는 경우
        wolf = wolf_graph[v] - sheep
        if wolf > 0:
            wolf_graph[v] = wolf
            sheep = 0
        else:
            sheep = wolf*(-1)
            wolf_graph[v] = 0
    else:
        sheep += sheep_graph[v]
    
    return sheep


    
answer = dfs(1)
print(answer)

    

    
            
"""
dfs문 돌기 
1부터 시작해서 리프노드까지 이동하기
리프노트에 이동했다면
return으로 남아있는 양의 수를 전달받기
동적으로 양의 수와 늑대의 수를 바꿔주기
"""   

        

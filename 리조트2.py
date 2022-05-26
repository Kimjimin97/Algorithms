import sys
input = sys.stdin.readline
N, M = map(int, input().split())

graph =[ [ float("Inf") for _ in range(N*2)]  for _ in range(1,N+9)]


n_cou = N*2-2

impossible = list(map(int, input().split()))

graph[0][0] = 0


# day차에 리조트에 들어가기 위해 계산된 금액
for day in range(N):
    for c in range(n_cou):
        if day+1 in impossible:
            graph[day+1][c] = min(graph[day+1][c], graph[day][c])
        
        else:
            graph[day+1][c] = min(graph[day][c]+10000, graph[day+1][c])

            for a in range(1,4):
                graph[day+a][c+1] = min(graph[day][c]+25000, graph[day+a][c+1])
            
            for b in range(1,6):
                graph[day+b][c+2] = min(graph[day][c]+37000, graph[day+b][c+2])
            
            if c >= 3:
                graph[day+1][c-3] = min(graph[day][c], graph[day+1][c-3])

print(min(graph[N]))
        


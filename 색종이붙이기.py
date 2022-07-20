




graph = []
items = []

paper = [0,5,5,5,5,5]

for i in range(10):
    lists = list(map(int, input().split()))
    graph.append(lists)
    for j in range(10):
        if graph[i][j] == 1:
            items.append([i,j])


def paint(x,y,k):
    global visited
    global paper
    nvisited = []
    for i in range(k):
        for j in range(k):
            if x+i <0 or y+j < 0 or x+i >= 10 or y+j >= 10:
                return []
            if graph[x+i][y+j] != 1 or visited[x+i][y+j]:
                return []
            nvisited.append([x+i,y+j])
        
    paper[k] -= 1
    if paper[k] < 0:
        paper[k] += 1
        return []
            
    return nvisited
            

visited = [[False]*10 for _ in range(10)]
answer = float("Inf")


def dfs(L,cnt):
    global answer
    global visited

    for g in visited:
        print(g)
    print()
    if L == len(items):
        answer = min(answer,cnt)
        return

    x,y = items[L]
    if visited[x][y]:
        dfs(L+1,cnt)
        return
        

    for k in range(5):
        if len(paint(x,y,k+1)) == 0:
            continue
        else:
            nvisited = paint(x,y,k+1)
            for nx, ny in nvisited:
                visited[nx][ny] = True

            dfs(L+1, cnt + 1)
            for nx, ny in nvisited:
                visited[nx][ny] = False
    
            

dfs(0,0)
if answer == float("Inf"):
    print(-1)
else:
    print(answer)




N,M ,R =map(int, input().split())

graph = []


for _ in range(N):
    graph.append(list(map(int, input().split())))

for _ in range(R):
    for s in range(min(N,M)//2):
        x,y =s,s
        tmp = graph[x][y]

        ## 아래 이동
        for i in range(x+1,x+N-2*s ):
            x = i
            prev_val= graph[x][y]
            graph[x][y] = tmp 
            tmp = prev_val 

        
        ## 오른쪽
        for j in range(y+1, y+M-2*s):
            y = j
            prev_val = graph[x][y]
            graph[x][y] = tmp
            tmp = prev_val 
        
        ## 위쪽 이동
        for i in range(x-1, x-(N-2*s),-1):
            x = i
            prev_val =graph[x][y]
            graph[x][y] = tmp 
            tmp = prev_val
        
        ## 왼쪽 이동 
        for j in range(y-1,y-(M-2*s),-1 ):
            y = j 
            prev_val = graph[x][y]
            graph[x][y] = tmp 
            tmp = prev_val
        
for g in graph:
    print(*g)

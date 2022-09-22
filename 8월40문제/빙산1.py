N,M  = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))


### 빙산의 각 부분에 해당되는 칸에 있는 높이는 일년마다 그 칸에 동서남북 
## 네 방향으로 붙어있는 0이 저장된 칸의 갯수만큼 줄어든다.
## 각 칸에 저장된 높이는 0보다 ㅈ
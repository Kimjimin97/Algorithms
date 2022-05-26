T = int(input())

R, C = map(int, input().split())

# R개의 줄에 걸쳐 c-1개 정수가 주어짐,  
# C개의 서버 좌우로 연결하는 통신망을 설치하는 비용

# R-1개의 C개의 정수
# i번째 행과 i+1번째 행에 놓은 C개의 서버를 상하로 연결하는 통신망을 설치하는 비용



for t in range(T):
    graph = [[]*1000 for i in range(1000)]
    for i in range(R):
        li = list(map(int, input().split()))
        for j in range(C-1):
            print(i*C+j, i*C+j+1)
            # graph[i*C+j][i*C+j+1] = li[j]
        
    for i in range(R-1):
        li = list(map(int, input().split()))
        for j in range(C):
            print(i*C+j, i*C+C+1)
            # graph[i*C+j][i*C+C+j] = li[j]
    # print(graph)
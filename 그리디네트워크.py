import heapq
T = int(input())



# R개의 줄에 걸쳐 c-1개 정수가 주어짐,  
# C개의 서버 좌우로 연결하는 통신망을 설치하는 비용

# R-1개의 C개의 정수
# i번째 행과 i+1번째 행에 놓은 C개의 서버를 상하로 연결하는 통신망을 설치하는 비용
answers = []

def union(a,b):
    root1 = find(a)
    root2 = find(b)
    if root1 < root2:
        parent[root2] = root1
    else:
        parent[root1] = root2
    
    

def find(u): # 부모 노드 찾기
    if u != parent[u]:
        parent[u] = find(parent[u])
    return parent[u]

for _ in range(T):
    R, C = map(int, input().split())
    costs = []

    for i in range(0,R*C,C):
        input_li = list(map(int,input().split()))
        for j in range(C-1):
            heapq.heappush(costs,(input_li[j],i+j,i+j+1))


    for a in range(0,R*C-C,C):
        input_li = list(map(int, input().split()))
        for b in range(C):
            heapq.heappush(costs,(input_li[b],a+b,a+b+C))
    

    answer = 0
    parent = [i for i in range(R*C)]

    while costs:
        c, a,b = heapq.heappop(costs)
        if find(a) != find(b):
            union(a,b)
            answer += c
    
    answers.append(answer)

print(*answers)
# 데이터 삽입







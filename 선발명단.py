'''
dfs 시간 복잡도
'''
T = int(input())

answer = float("-Inf")

def dfs(person,sum):
    global answer, visited
    
    if person == 11:
        answer = max(answer, sum)
        return
    
    for i in link[person]:
        if not visited[i]:
            visited[i] = True
            dfs(person+1, sum+graph[person][i])
            visited[i] = False
        
    

for _ in range(T):
    graph = []
    link = [[] for _ in range(11)]

    for i in range(11):
        lists = list(map(int, input().split()))
        graph.append(lists)
        for j in range(len(lists)):
            if lists[j] != 0:
                link[i].append(j)

    answer = float("-Inf")
    visited = [False]*11
    dfs(0,0)
    print(answer)
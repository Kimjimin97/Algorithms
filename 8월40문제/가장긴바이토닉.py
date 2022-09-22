N = int(input())

lists = list(map(int, input().split()))
answer = 0

graph = [[1]*N for _ in range(N)]


def left_check(k):
    global graph
    _max = 0
    for i in range(k):
        if lists[i] < lists[k]:
            for j in range(i):
                if lists[j] < lists[i] and lists[j] < lists[k] :
                    graph[k][i] = max(graph[k][i],graph[k][j]+1)

            _max = max(graph[k][i],_max)
    
    return _max

def right_check(k):
    global graph
    _max = 0
    for i in range(k+1,N):
        if lists[i] < lists[k]:
            for j in range(k+1,i):
                if lists[j] > lists[i] and lists[j] < lists[k]:
                    graph[k][i] = max(graph[k][i],graph[k][j]+1)

            _max = max(graph[k][i],_max)
    
    return _max


for k in range(N):
    answer = max(answer, left_check(k) + right_check(k))




print(answer+1)


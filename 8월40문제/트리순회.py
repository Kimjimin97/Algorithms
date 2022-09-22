## 중위 순회 O(N) 유사 중위 순회 O(N)
import sys
limit_number = 10**6
sys.setrecursionlimit(limit_number)
input = sys.stdin.readline
N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N):
    a,b,c = map(int, input().split())
    graph[a].append(b)
    graph[a].append(c)


## 중위 순회

middle_lists = []
def middle(v):
    global middle_lists
    if v == -1:
        return
    
    middle(graph[v][0])
    middle_lists.append(v)
    middle(graph[v][1])

middle(1)
last_node = middle_lists[-1]

cnt = 0
similar_lists = []
end_flag = False

similar_lists = []
first_flag = True


def similar(v):
    global similar_lists
    global cnt
    global end_flag
    global first_flag
    if graph[v][0] != -1:
        # //  이 부분에서 현재 노드에서 다른 노드로 이동한다.
        cnt += 1
        similar(graph[v][0])
    
    
    if graph[v][1] != -1:
        cnt += 1
        similar(graph[v][1])
    
    
    if v == last_node:
        print(cnt)
        exit(0)
    cnt += 1
    


similar(1)
print(cnt)
    
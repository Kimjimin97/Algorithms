import sys
sys.setrecursionlimit(3000)
def input():
    return sys.stdin.readline().rstrip()

def get_diameter():
    result = 0
    visited = [0 for _ in range(N)]
    def dfs(node, tag):
        nonlocal visited
        stack = [(node,0)]
        visited[node] += 1
        max_node = -1
        max_dis = 0
        while stack:
            node, dis = stack.pop()
            if dis > max_dis:
                max_dis = dis
                max_node = node
            for next_node in graph[node]:
                if visited[next_node] == tag:
                    visited[next_node] += 1
                    stack.append((next_node,dis+graph[node][next_node]))
        return [max_node, max_dis]
    
    for idx in range(N):
        if visited[idx] == 0:
            far_node,_ = dfs(idx,0)
            _,dis = dfs(far_node ,1)
            result += dis



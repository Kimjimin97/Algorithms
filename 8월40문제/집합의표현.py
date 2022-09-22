import sys

input= sys.stdin.readline
sys.setrecursionlimit(10**7)

n,m = map(int, input().split())



graph = []
parent = [i for i in range(n+1)]

def union(a,b):
    a_parent =find(a)
    b_parent =find(b)

    parent[b_parent] = a_parent


def find(v):
    if v == parent[v]:
        return v 
    
    parent[v] = find(parent[v])
    return find(parent[v])


for _ in range(m):
    x, a,b = map(int, input().split())

    if x == 0:
        union(a,b)

    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")



# 노드 번호 - 부모노드의 번호로 리스트 생성

# 노드가 생성되면 두개의 노드 중 더 작은 값을 부모 노드로 갱신

# 재귀를 사용해서 노드와 부모 노드가 같은 노드까지 찾아서 갱신해 준다.

# 여기까지 union

# find는 2개의 노드를 이용해서 부모가 같은지 확인해 주기


def find_parent(x): # 노드 x 부모 찾기
    if parent[x] != x: # 해당 노드와 값이 같다면 부모노드를 찾은 것이다.
        parent[x] = find_parent(parent[x]) 
    
    return parent[x]

def unino_parent(a,b): # a b 두개의 노드가 들어왔다면
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

    


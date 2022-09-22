N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

## 만약 한번이라도 부딪혀서 합쳐진 경우면 따로 체크를 해준다.

dxy = [[-1,0],[0,1],[1,0],[0,-1]]

## 조합함수

def move_oneblock(i,j,k):
    

def move(k):
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 :
                move_onblock(i,j,k)


def check_simul():
    for it in lists:
        for k in it:
            move(k)
    return

# dir_lists = [i for i in range(4)]
lists = []
def dfs():
    global lists
    print(lists)
    if len(lists) == 5:
        check_simul(lists)
        return
    
    for k in  range(4):
        lists.append(k)
        dfs()
        lists.pop()

dfs()


from pickle import GLOBAL


N,M,H = map(int, input().split())

exist = [[False]*(N) for _ in range(H)]

for _ in range(M):
    a,b = map(int, input().split())
    exist[b-1][a-1] = True 

res = float("Inf")

visited = [[False]*N for _ in range(H)]
dxy =[[0,1],[0,-1],[1,0],[-1,0]]

print(exist)
def check(): # i번 세로선이 i번으로 도착하는지 확인
    for i in range(N):
        temp = i     # 이동하는 세로선 위치
        for j in range(H):
            print(j,temp)
            if exist[j][temp]:  # 오른쪽이 1인 경우
                temp += 1
            elif temp > 0 and exist[j][temp - 1]: # 왼쪽이 1인 경우
                temp -= 1
        
        if temp != i:
            return False
    return True
    
res = float("Inf")
        


def dfs(x,y,n):
    global res
    print(x,y,n)
    if n > 3:
        return
    
    if check():
        res = min(res, n)
        return
    
    for i in range(x,H):
        if x == i:
            k = y
        else:
            k = 0
        
        for j in range(k,N-1): ## 마지막 인덱스는 제거해 주어야 한다.
            if not exist[i][j]:
                exist[i][j] = True
                dfs(i, j+2 , n+1 )
                exist[i][j] = False


dfs(0,0,0)


if res == float("Inf"):
    print(-1)
else:
    print(res)
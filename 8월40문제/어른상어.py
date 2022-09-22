N, M , K = map(int, input().split())

## 상어위치
now_shark =  [[400]*N for _ in range(N)]

## 상어 번호와 냄새 시간 저장
smell_graph = [[[] for _ in range(N)] for _ in range(N)]

for i in range(N):
    lists1 = list(map(int, input().split()))
    for j in range(N):
        if lists1[j] != 0:
            
            smell_graph[i][j] = [lists1[j]-1,K] 
            now_shark[i][j] = lists1[j]-1


now_dir = list(map(int, input().split()))

for i in range(M):
    now_dir[i] -= 1

like_dir = []
for _ in range(M):
    lists = []
    for i in range(4):
        lists.append(list(map(int, input().split())))
    like_dir.append(lists)

dxy = [[-1,0],[1,0],[0,-1],[0,1]]
new_shark = [[401]*N for _ in range(N)]


def move_shark(i,j,nx,ny,kk):
    global new_shark
    ## 선택한 방향에 냄새가 없으면 무조건 이동
    new_shark[nx][ny] = min(new_shark[nx][ny], now_shark[i][j])
    now_dir[now_shark[i][j]] = kk
    print(new_shark)




def pick_one_dir(candidate,i,j):
    for kk in like_dir[now_shark[i][j]][now_dir[now_shark[i][j]]]:
        kk -= 1
        if kk in candidate:
            nx, ny = i +dxy[kk][0], j+dxy[kk][1]
            ## 선택한 방향으로 움직이기
            move_shark(i,j,nx,ny,kk)
            return


def pick_dir():
    global new_shark
    new_shark = [[400]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ## 현재 상어가 존재 한다면 이동 방향을 정해준다.
            if now_shark[i][j] != 400:
                ## 아무 냄새도 없는칸
                no_candidate = []
                ## 자신의 냄새가 있는 칸
                me_candidate = []

                for k in range(4):
                    nx, ny = i+dxy[k][0], j+dxy[k][1]
                    if nx  <0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if not smell_graph[nx][ny]:
                        no_candidate.append(k)
    
                    elif smell_graph[nx][ny][0] == now_shark[i][j]:
                        me_candidate.append(k)          
                
                ## 가능한 칸이 여러 개일 경우
                if no_candidate:
                    pick_one_dir(no_candidate,i,j)

                
                elif me_candidate:
                    pick_one_dir(me_candidate,i,j)


    print("RR",new_shark)
    print()
    for g in new_shark:
        print(g)
    print()
    return new_shark
                    

def check_num():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if now_shark[i][j] > 0 and now_shark[i][j] != 400:
                cnt += 1
    
    if cnt == 0 :
        return True
    return False 


def update_time():
    global smell_graph
    global now_shark
    for i in range(N):
        for j in range(N):
            ## 냄새가 비어 있지 않는 경우
            if smell_graph[i][j]:
                a,b = map(int, smell_graph[i][j])
                ## 시간 줄이기
                b-= 1
                if b == -1:
                    smell_graph[i][j] = []
                    continue

                smell_graph[i][j] = [a,b]
                # print(smell_graph[i][j], a,b)
            if now_shark[i][j] >= 0 and now_shark[i][j] < 400:
                smell_graph[i][j] = [now_shark[i][j],K]


answer = 0
while answer <= 100:
    ## 0번 상어가 보다 수가 큰 상어의 갯수가 몇개인지 확인

    

    update_time()

    print(answer)
    for g in now_shark:
        print(g)
    print()

    if check_num():
        break
    ## 다음 단계 진행
    answer += 1
    
    ## 이동 방향 선택
    now_shark = pick_dir()
    
print(answer)
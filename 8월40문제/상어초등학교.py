## 서ㄴ생님은 학ㅇㅢ 순ㅓㅡㄹ 정ㅐ고,
## 각학생이 좋아하는 학ㅇ 4명도 조
## 다음과 같은 규칙을 이용해 정해진 순ㅓㅐ로 학ㅇㅢ 자를 정ㅏ


## 비어있는 칸  중에서 좋ㅏ하는 학생이 인ㅂㅏㄴ


N = int(input())

friend_graph = []
node = [[] for _ in range(N*N+1)]

for _ in range(N*N):
    friend_graph.append(list(map(int, input().split())))

graph = [[-1]*N for _ in range(N)]

dxy = [[1,0],[-1,0],[0,1],[0,-1]]


def check_four(x,y,friends):
    check_blank, check_friend = 0,0
    for k in range(4):
        nx, ny = x+dxy[k][0], y+dxy[k][1]
        if nx < 0 or ny < 0 or nx >=N or ny >= N:
            continue
        if graph[nx][ny] == -1:
            check_blank += 1
        if graph[nx][ny] in friends:
            check_friend += 1
    return  check_friend, check_blank

for g,f1,f2,f3,f4 in friend_graph:
    friend, blank ,x,y= float("-INF"), float("-INF"),-1,-1
    node[g].extend([f1,f2,f3,f4])
    for i in range(N):
        for j in range(N):
            if graph[i][j] != -1:
                continue

            flag = False
            check_friend, check_blank = map(int, check_four(i,j,[f1,f2,f3,f4]))
            if check_friend > friend:
                flag= True
            elif check_friend == friend:
                if check_blank > blank :
                    flag= True
                elif check_blank == blank :
                    if i < x:
                        flag= True
                    elif i == x:
                        if j < y:
                            flag = True
            
            if flag:
                friend,blank,x,y = check_friend,check_blank,i,j
    graph[x][y] = g

match_score = {
    0:0,
    1:1,
    2:10,
    3: 100,
    4: 1000
}


answer = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        for k in range(4):
            nx, ny = i+dxy[k][0], j+dxy[k][1]
            if nx <0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] in node[graph[i][j]]:
                cnt += 1
        answer += match_score[cnt]

print(answer)


            




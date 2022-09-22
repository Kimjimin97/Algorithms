## 크기가 무한인 정사각형 모눈종이가 있다.
## 모눈 종이의 각 정사각형은 행과 열의 쌍으로 표현할 수 있다.
## 모눈 종이 전체를 양의 정수의 소용돌이 모양으로 채울 것이다. ]

## 일단 숫자 1을 0행 0열에 쓴다.
## 그리고 나서 0행 1열에 숫자 2를 쓴자.
## 거기서 부터 소용돌이는 반시계 방향으로 시작된다

N =10000
graph = [[-1]*(N+1) for _ in range(N+1)]

x = 5
y =5

dxy = [[-1,0],[0,-1],[1,0],[0,1]]
input_num = 1

r1,c1,r2,c2 = map(int, input().split())
r1,c1,r2,c2 = r1 +5000,c2+5000,r2+5000,c2+5000

print(r1,c1,r2,c2)

def go_up(n,k):
    global x
    global y
    global input_num
    global graph

    for _ in range(n):
        x, y = x +dxy[k][0], y + dxy[k][1]
        input_num += 1
        graph[x][y] = input_num 
       
    return 


rotate_num = 0
graph[x][y] = 1
for _ in range(N//2):
    y += 1
    rotate_num += 2
    input_num += 1
    graph[x][y] = input_num


    go_up(rotate_num-1,0)

    for i in range(1,4):
        go_up(rotate_num,i)

for g in graph:
    print(g)
    
# for i in range(r1,r2+1):
#     for j in range(c1,c2+1):
#         print(graph[i][j], end = " ")
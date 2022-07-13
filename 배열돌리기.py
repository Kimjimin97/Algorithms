import copy
N, R = map(int, input().split())

N = 2**N

board = [list(map(int, input().split())) for _ in range(N)]

newb = [[0]*N for _ in range(N)]

command = []

for _ in range(R):
    command.append(list(map(int, input().split())))


def work1(l):
    global newb, board
    n = 2**l
    for sx in range(0,N,n):
        for sy in range(0, N, n):
            for i in range(n):
                for j in range(n):
                    ## 마지막 줄 (sx + n - 1) - 거꾸로 올라가기(j) 
                    newb[sx+i][sy+j] = board[sx+n-1-i][sy+j] 

def work2(l):
    global newb, board
    n = 2**l
    for sx in range(0,N,n):
        for sy in range(0, N, n):
            for i in range(n):
                for j in range(n):
                    ## 마지막 줄 (sx + n - 1) - 거꾸로 올라가기(j) 
                    newb[sx+i][sy+j] = board[sx+i][sy+n-j-1] 
            


## 오른쪽 90도 회전
def work3(l):
    global newb, board
    n = 2**l
    for sx in range(0,N,n):
        for sy in range(0, N, n):
            for i in range(n):
                for j in range(n):
                    newb[sx+i][sy+j] = board[sx+n-1-j][sy+i]
## 왼쪽 90도 회전
def work4(l):
    global newb, board
    n = 2**l
    for sx in range(0,N,n):
        for sy in range(0, N, n):
            for i in range(n):
                for j in range(n):
                    newb[sx+i][sy+j] = board[sx+j][sy+n-1-i]


def work5(l):
    global newb, board
    n = 2**l
    for sx in range(0,N,n):
        for sy in range(0, N, n):
            for i in range(n):
                for j in range(n):
                    newb[sx+i][sy+j] = board[N-n-sx+i][sy+j]

def work6(l):
    global newb, board
    n = 2**l
    for sx in range(0,N,n):
        for sy in range(0, N, n):
            for i in range(n):
                for j in range(n):
                    newb[sx+i][sy+j] = board[sx+i][N-n-sy+j]

def work7(l):
    global newb, board
    n = 2**l
    for sx in range(0,N,n):
        for sy in range(0, N, n):
            for i in range(n):
                for j in range(n):
                    newb[sx+i][sy+j] = board[N-sy-n+i][sx+j]

def work8(l):
    global newb, board
    n = 2**l
    for sx in range(0,N,n):
        for sy in range(0, N, n):
            for i in range(n):
                for j in range(n):
                    newb[sx+i][sy+j] = board[sy+i][N-sx-n+j]

for k,l in command:
    if k ==1:
        work1(l)

    elif k == 2:
        work2(l)

    elif k == 3:
        work3(l)

    elif k == 4:
        work4(l)

    elif k == 5:
        work5(l)

    elif k == 6:
        work6(l)

    elif k == 7:
        work7(l)

    elif k == 8:
        work8(l)
    board = copy.deepcopy(newb)
    
    # print(l,k)
    # for g in newb:
    #     print(g)
    # print()


for g in newb:
    print(*g)





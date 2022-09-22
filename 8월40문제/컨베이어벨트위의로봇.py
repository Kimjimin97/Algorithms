import sys
input = sys.stdin.readline
N, K = map(int, input().split())

graph = list(map(int, input().split()))
robot = [False]*N
answer = 0
def check_k():
    cnt = 0
    for k in graph:
        if k == 0:
            cnt += 1
    if cnt >= K :
        return True
    return False


while True:
    
    if check_k():
        print(answer)
        break

    answer += 1
    graph.insert(0,graph.pop())
    robot.insert(0, robot.pop())

    robot[-1] = False 
    for i in range(N-2, -1,-1):
        if robot[i] == True and robot[i+1] == False:
            if graph[i+1] > 0:
                robot[i] = False 
                robot[i+1] = True
                graph[i+1] -= 1
        robot[-1] = False
    
    if graph[0] > 0 :
        graph[0] -= 1
        robot[0] = True


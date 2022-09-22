from collections import deque

n, k = map(int,input().split())
A = list(map(int,input().split()))
belt = deque()
belt.extend(A)
robot = [False] * n


def run_belt(belt,robot):
    belt.rotate(1)
    robot = deque(robot)
    robot.rotate(1)
    robot = list(robot)
    return belt, robot

def move_robot(belt,robot):
    belt = list(belt)
    for i in range(n-2,-1,-1):
        if robot[i] and not robot[i+1] and belt[i+1]:
            robot[i] = False
            if i+1 != n-1: robot[i+1] = True 
            belt[i+1] -= 1
    belt = deque(belt)
    return belt, robot

def robot_on(belt,robot):
    if not robot[0]:
        x = belt.popleft()
        if x:
            x -= 1
        belt.appendleft(x)
        robot[0] = True
    return belt, robot

def count_zero(belt):
    if belt.count(0) >= k:
        return True
    return False


cnt = 1
while True:
    cnt += 1
    belt, robot = run_belt(belt,robot)
    belt, robot = move_robot(belt,robot)
    belt, robot = robot_on(belt,robot)
    print(robot)
    print(belt)
    print()
    if count_zero(belt):
        print(cnt)
        break
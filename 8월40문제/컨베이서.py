n,k = map(int, input().split())

belt = list(map(int, input().split()))

robot_idx = [0]*n 


res = 1

cnt = 0
while True:
    belt.insert(0,belt.pop(-1))

    robot_idx.inser(0,0)
    robot_idx.pop(-1)
    robot_idx[-1] = 0

    for i in range(2,n+1):
        if robot_idx[i] != 0:

from collections import deque


print(1%7)
T = int(input())

for _ in range(T):
    n = int(input())
    before = [-1]*n
    method = [-1]*n
    visited = [False]*n
    queue = deque()
    queue.append(1%n)
    visited[1%n] = True
    method[1%n] = 1
    
    while queue:
         now = queue.popleft()
         for  i in [0,1]:
            next = (now*10+i)%n
            if not visited[next]:
                visited[next] = True
                before[next] = now
                method[next] = i

    if not visited[0]:
        print('BRAK')

    else:
        ans = ''
        i = 0
        while i !=-1:
            ans += str(method[i])
            i = before[i]
#         print(ans[::-1])



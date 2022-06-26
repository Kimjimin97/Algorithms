

N, B, W = map(int, input().split())

graph = list(map(str,input()))

left = 0
right = 0
black = 0
white = 0
answer = float("-Inf")

while True:
    right += 1
    if graph[right] == "W":
        white+=1
    else:
        black += 1
    
    if black > B:
        for k in range(left, right):
            if graph[k] != 'B':
                left += 1
                white -= 1
            elif graph[k] == "B":
                left += 1
                black -= 1
                break
    
    if white >= W and black <= B:
        answer = max(answer, right - left + 1)
    
    if right == N-1:
        break
    
if answer == float("-Inf") :
    print(0)
else:
    print(answer)
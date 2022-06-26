from itertools import permutations

n,x,y = map(int, input().split())

items = list(permutations([i for i in range(1, 2*n+1)]))
answer = 0


for it in items:
    flag = True
    for k in range(0,len(it),2):
        if it[k+1] < it[k]:
            flag= False
            break
        if it[k+1] - it[k]-1 != k//2 +1:
            flag= False
            break
        if it[k+1] == x or it[k]== x:
            x_value= k
        if it[k+1] == y or it[k] ==y:
            y_value= k

    if flag:
        if x_value== y_value :
            answer +=1

print(answer)
            
        
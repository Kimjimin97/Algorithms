from distutils import unixccompiler
import genericpath
import tempfile


graph = [[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]]


n = 4

def right(start_x, start_y):
    global graph
    tmp = graph[start_x][start_y]
    for y in range(start_y, start_y+n-1):
        prev_val = graph[start_x][y+1]
        graph[start_x][y+1] = tmp
        tmp = prev_val
    
    return start_x, y, tmp

def down(start_x, start_y, tmp):
    global graph 
    for x in range(start_x, start_x+n-1):
        prev_val = graph[x+1][start_y]
        graph[x+1][start_y] = tmp 
        tmp = prev_val 
    
    return x, start_y, tmp

def left(start_x, start_y, tmp):
    global graph 
    for y in range(start_y, start_y-(n-1), -1):
        prev_val = graph[start_x][y-1]
        graph[start_x][y-1] = tmp 
        tmp = prev_val
    
    return start_x, y, tmp


def up(start_x, start_y, tmp):
    global graph 
    for x in range(start_x, start_x-(n-1), -1):
        prev_val = graph[x-1][start_y]
        graph[x-1][start_y] = tmp 
        tmp = prev_val
    return x, start_y, tmp

for g in graph:
    print(g)

start_x, start_y, tmp = right(0,0)

start_x, start_y, tmp = down(start_x, start_y+1, tmp)
start_x, start_y, tmp = left(start_x+1, start_y, tmp)
print(start_x, start_y, tmp)
start_x, start_y, tmp = up(start_x, start_y-1, tmp)

for g in graph:
    print(g)
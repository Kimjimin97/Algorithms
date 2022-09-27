

graph = [[""]*6 for _ in range(6)]
merge_dict = dict()
parent = dict()

def indict(r,c):
    if (r,c) in parent.keys():
        return True
    return False

def make_dict(r,c):
    global parent
    if (r,c) not in parent.keys():
            parent[(r,c)] = (r,c)

def find(v):
    global parent
    if v == parent[v]:
        return v
    parent[v] = find(parent[v])
    return find(parent[v])
    


def merge(r1,c1,r2,c2,value):
    global graph
    global parent
    A = (r1,c1)
    B = (r2,c2)
    a_parent = find(A)
    b_parent = find(B)
   
    graph[r2][c2] = value
    parent[b_parent] = a_parent


def update_v(r,c,value):
    global graph
    graph[r][c] = value
    if (r,c) in parent.keys():
        A = find((r,c))
        graph[A[0]][A[1]] = value
    else:
        graph[r][c] = value

def update_vv(value1, value2):
    global graph
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == value1:
                if indict(i,j):
                    A = find((i,j))
                    graph[A[0]][A[1]] = value2
                else:
                    graph[i][j] = value2

def unmerge(r,c):
    global graph
    global parent
    if not indict(r,c):
        return 
    A = (r,c)
    B = find(A)
    value =  graph[B[0]][B[1]]
    lists = []
    for i in range(len(graph)):
        for j in range(len(graph)):
            # if i == r and j == c:
            #     continue
            if (i,j) in parent.keys():
                if find((i,j)) == B :
           
                    C = (i,j)
                    lists.append(C)
                    graph[i][j] = ""
    graph[r][c] =  value
    parent[(r,c)] = (r,c)
    for g in lists:
        del parent[g]
                    

def solution(commands):
    global merge_dict
    global graph
    answer = []

    for c in commands:
        print(answer)
        print(parent)
        for g in graph:
            print(g)
        print()
        print(c)
        c = list(map(str, c.split()))
        if c[0] == "UPDATE":
            if len(c) == 4:
                update_v(int(c[1]), int(c[2]), c[3])
            else:
                update_vv(c[1],c[2])
            continue

        if c[0] == "MERGE":
            r1,c1,r2,c2 = int(c[1]),int(c[2]),int(c[3]),int(c[4])
            flag = False
            
            if indict(r1,c1):
                A = find((r1,c1))
                value = graph[A[0]][A[1]]
                flag = True
            elif graph[r1][c1]:
                value = graph[r1][c1]
                flag = True
            elif indict(r2,c2):
                A = find((r2,c2))
                value = graph[A[0]][A[1]]
                flag = True
            elif graph[r2][c2]:
                value = graph[r2][c2]
                flag = True
            
            if not flag:
                value = "" 

            make_dict(r1,c1)
            make_dict(r2,c2)
            merge(r1,c1,r2,c2,value)
            continue

        if c[0] == "UNMERGE":
            r,c = int(c[1]),int(c[2])
            unmerge(r,c)
            continue
        

        if c[0] == "PRINT":
         
            r,c = int(c[1]),int(c[2])
            if (r,c) in parent.keys():
                print(parent)
                A = find((r,c))
                answer.append(graph[A[0]][A[1]])
            else:
                if graph[r][c]:
                    answer.append(graph[r][c])
                else:
                    answer.append("EMPTY")
        print(c)
        
    
    return answer

print(solution(
["UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "MERGE 2 1 2 2", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4","UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UNMERGE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "UNMERGE 1 2", "MERGE 1 3 1 4", "UPDATE korean hansik", "MERGE 1 3 1 1", "UNMERGE 1 4", "PRINT 2 1", "PRINT 1 4"]))
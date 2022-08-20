import sys
input =sys.stdin.readline
U , F = map(int, input().split())

groups = dict()

for _ in range(U):
    people = list(map(str, input().split()))
    user = people[0]
    
    in_group = [user]

    if len(people) >1:
        in_group += list(map(str, people[1].split(",")))

    for g in range(len(in_group)):
        if in_group[g] not in groups.keys():
            groups[in_group[g]] = [user]
        else:
            groups[in_group[g]].append(user)
            

file = dict()
for f in range(F):
    name, oper,owner,group = map(str, input().split())
    file[name] = [oper, owner, group]
    

def mapping(s):
    if s == "0":
        return_li = []
        return return_li
    elif s == "1":
        return_li = ["X"]
        return return_li
    elif s == "2":
        return_li = ["W"]
        return return_li
    elif s == "3":
        return_li = ["X", "W"]
        return return_li
    elif s == "4":
        return_li = ["R"]
        return return_li
    elif s == "5":
        return_li = ["R", "X"]
        return return_li
    elif s == '6':
        return_li = ["R","W"]
        return return_li
    else:
        return_li = ["R","W","X"]
        return return_li
    
Q = int(input())
for q in range(Q):
    flag= False
    check_name, check_file, check_type = map(str, input().split())
    if check_file in file.keys():
        oper, ower, group = file[check_file]

        if check_name == ower:
            if check_type in mapping(oper[0]):
                flag= True
        elif group in groups.keys() and check_name in groups[group]:
            if check_type in mapping(oper[1]):
                flag= True
        else:
            if check_type in mapping(oper[2]):
                flag= True
    
    if flag:
        print(1)
    else:
        print(0)
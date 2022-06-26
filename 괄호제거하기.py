N = str(input())

n = 0
for ss in N:
    if ss == "(" :
        n+= 1



def back(delete,s):
    find = n
    if not delete:
        return
    
    while True:
        if find == 0:
            break

        for k in range(len(s)):
            if s[k] == ")":
                if find in delete:
                    s = s[:k] + s[k+1:]
                find -= 1
                break

    print(s)


def dfs(L,delete,s):
    if L >= n+1:
        return

    back(delete,s)

    
    for i in range(len(s)):
        if s[i] == "(":

            delete.append(L)
            dfs(L+1, delete,s[:i]+s[i+1:])
            delete.pop()
            dfs(L+1, delete,s)

dfs(1,[],N)
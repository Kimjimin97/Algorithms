import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

N = list(map(int, input()))

ten = 0

for i in range(len(N)):
    ten += N[i]*8**(len(N)-(i+1))


def dfs(n):
    if n <= 0:
        return
    
    dfs(n//2)
    print(n%2, end = "")

dfs(ten)
print()
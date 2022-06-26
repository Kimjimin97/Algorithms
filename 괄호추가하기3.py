N = int(input())

lists = list(input())

print(N)
print(lists)

graph = [[]*(N) for _ in range(N)]

for i in range(0,N,2):
    for j in range(i+1,N,2):
        if i == j:
            
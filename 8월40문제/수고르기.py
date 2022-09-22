import sys
input = sys.stdin.readline
N,M = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))

A.sort()

i, j = 0, 1
min_value= float("INF")

while True:
    if j == N-1 and abs(A[j]-A[i]) < M:
        print(min_value)
        break

    elif abs(A[j]-A[i]) == M:
        print(M)
        break
    elif abs(A[j]-A[i]) < M:
        j += 1
        
    elif abs(A[j]-A[i]) > M:
        min_value = min(min_value, abs(A[j]-A[i]))
        i += 1
              

import sys
input = sys.stdin.readline

N = int(input())
items = []


for _ in range(N):
    items.append(int(input()))

items.sort(reverse=True)

answer = sum(items)


for i in range(2,len(items),3):
    answer -= items[i]

print(answer)
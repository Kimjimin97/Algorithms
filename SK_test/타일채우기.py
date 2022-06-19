N = int(input())
lists = []
lists.append(0)
lists.append(2)
lists.append(7)
lists.append(22)

for i in range(2,N+1):
    lists.append((lists[i-1] *2 + lists[i-2] *7)%1000000007)

print(lists[N])


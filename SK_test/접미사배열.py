S = list(map(str, input()))

items = []

for i in range(len(S)):

    items.append(S[i:len(S)])

items.sort()

for k in items:
    print("".join(k))
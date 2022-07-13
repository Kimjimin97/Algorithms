## 치킨집 위치 저장
## 집 위치 저장

from itertools import combinations
N, M = map(int, input().split())

graph = []
house = []
chicken = []

for i in range(N):
    lists = list(map(int, input().split()))
    graph.append(list(lists))
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i,j))
        elif graph[i][j] == 2:
            chicken.append((i,j))

item = [i for i in range(len(chicken))]
items = list(combinations(item,M))

answer = float("Inf")

for it in items: ## 치킨집 M개
    ## 집에서 가장 가까운 치킨 집 찾기
    case_dist = 0
    for hx, hy in house:
        ## M개의 치킨집 중 가장 가까운 치킨 집까지 거리
        min_dist = float("Inf")
        for i in it:
            cx, cy = chicken[i][0], chicken[i][1]
            min_dist = min(min_dist, abs(cx-hx)+abs(cy-hy))
        case_dist += min_dist ## 그 집에서 가장 가까운 치킨집 거리 더하기
    answer = min(answer, case_dist)

print(answer)
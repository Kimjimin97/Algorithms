"""
맨 앞 뒤 행, 열 3개

짝수 행  2개
홀수 행 3개
"""

W,H=map(int, input().split())

graph = []

for _ in range(H):
    graph.append(list(map(int, input().split())))


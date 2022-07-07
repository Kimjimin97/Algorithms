"""
add c
문자열 뒤에 문자 c를 추가합니다.

del x
문자열 x번째 위치에 있는 글자를 삭제합니다.
문자열의 인덱스는 0부터 시작합니다. 
x 번째 위치에 문자를 삭제할 수 없는 경우에 오류가 발생합니다.

놀이 규칙
- 빈 문자열로 게임을 시작합니다
- 각 턴을 수행하는 사람은 1명입니다.
- 턴을 수행하는 사람은 가지고 있는 카드에 적혀있는 연산을 모두 수행하고 턴을 종료
- 오휴가 발생하면 문자열은 "error"가 되고, 즉시 게임이 종료됩니다.
- 게임이 끝났을 때, 문자열이 빈 문자열이라면, 문자열은 "empty"가 됩니다.


문자열 게임에 참가하는 사람은 N명이고, 카드는 C장 있습니다.

게임에 참가하는 사람이 어떤 순서대로 카드를 냈는지 알고 있을 때,
게임의 결과로 나올 수 있는 문자열을 사전순으로 출력

N,C // 참가 인원, 카드 갯수
1번 사람부터 N번 사람까지 낸 카드의 갯수와 카드 순서
3 2 4 5 // 2번째 사람이 3개의 카드 2,4,5를 순서대로 낸 것

## 로직
- 순열 실행 순서 설정하기
- 9! (순열) *9(연산 갯수)
"""
from itertools import permutations

N,C = map(int, input().split())

graph = []
cnt = 0
for _ in range(N):
    lists = list(map(int, input().split()))
    graph.append(lists)
    cnt += lists[0]

oper = []
for _ in range(C):
    oper.append(list(map(str, input().split(","))))


items = [i for i in range(N)] ## 사람 순서 정하기
item = list(permutations(items))

print(item)
## 사람 순서대로 연산 실행하기
answer = []
strings = ""
def calculate(cards):
    global strings
    cards = cards[1:]
    for card in cards:
        for k in oper[card-1]:
            a,b = map(str, k.split())
            if a == "ADD":
                strings += b
            elif a == "DEL":
                b= int(b)
                if len(strings) > b:
                    strings = strings[:b] + strings[b+1:]
                else:
                    return False 
    return True



for it in item:
    strings = ""
    for i in it:
        ## 연산 할 카드 뽑기
        cards = graph[i]

        ## 카드 연산하기
        if not calculate(cards):
            strings = "ERROR"
            break 
    answer.append(strings)

print(items)
answer.sort()       
for g in answer:
    print(g)
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

문제 이해를 잘 못했다.
턴을 수행하는 사람은 가지고 있는 카드에 적혀져 있는 연산을 모두 수행하고 턴을 종료합니다.
연산과 카드 순서를 헷갈렸다.

## 최종 로직
사람 인덱스 번호
1) 사람이 가지고 있는 카드 갯수 알기 
     - 사람 마다 가지고 있는 카드 수 저장
     - []
2) 그 만큼의 순열 생성하기  - 경우의 수 생성
3) 경우의 수만큼 연산 수행하기

나중에는 게임 종료 후 빈 문자열이면 EMPTY 출력하는 걸 깜박해서 많이 틀렸다..

"""
from itertools import permutations
import copy
N,C = map(int, input().split())

graph = []
cnt = 0
able = []
for i in range(N):
    ## 순열 시켜줄 리스트 생성 사람이 가지고 있는 카드 갯수 만큼 생성
    lists = list(map(int, input().split()))
    able += [i]*lists[0]
    lists.pop(0) ## 카드만 저장하기
    graph.append(lists)



oper = []
for _ in range(C):
    oper.append(list(map(str, input().split(","))))

item = list(permutations(able))


# ## 사람 순서대로 연산 실행하기
# answer = []
# strings = ""
def calculate(card):
    global strings

    for k in oper[card]:
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

answer = []
for it in item:
    strings = ""
    graphs = copy.deepcopy(graph)
    for i in it: ## 카드를 제출 할 사람 뽁기
        ## 연산 할 카드 뽑기
        card = graphs[i].pop(0) -1

    #     ## 카드 연산하기 
        if not calculate(card):
            strings = "ERROR"
            break 
    
    if strings == "":
        answer.append("EMPTY")
    else:
        answer.append(strings)


answer.sort()
answer =set(answer)       
for g in answer:
    print(g)
## 마법사 상어가 크기

## 말의 갯수가 유동적이다.

## 로직

"""
말들 만들기
for 문으로 말들 이동하기

이동이 모두 끝난 후에 2개 이상이면 파이어볼을 나눈다.

"""
import copy
from pickle import FALSE
horse = []

N,M,K = map(int, input().split())

horse = []
## r,c,m,s(거리),d(속력)
for i in range(M):
    r,c,m,s,d = map(int, input().split())
    horse.append([r-1,c-1,m,s,d])
   

dxy = [[-1,0],[-1,1],[0,1],
[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

tcnt = 0

# cnt가 K번 실행
while tcnt < K:
    nhorse = []
    ## 같은 위치에 있는 말 찾기
    loca = dict()
    ## 말 이동
    for r,c,m,s,d in horse:
        for ss in range(s):
            r,c = r +dxy[d][0], c+dxy[d][1]

        r = r%N
        c = c%N
        if (r,c) in loca.keys():
            loca[(r,c)].append([m,s,d])

        else:
            loca[(r,c)] = [[m,s,d]]


    ## 말들을 나누는 과정
    for a in loca.keys():
        ## 질량의 합, 속력의 합, 파이어볼 갯수
        nr,nc = a[0],a[1]
        if len(loca[a]) < 2:
            nhorse.append([nr,nc]+loca[a][0])

        elif len(loca[a]) >= 2:
            flag = True
    
            sum_m, sum_s, cnt,sum_d = 0,0,0,0
            for m,s,d in loca[a]:
                cnt += 1
                sum_m += m
                sum_s += s
                sum_d += d
    
            if sum_d//2 != 0:
                if cnt//2 == 0:
                    flag = False 

            if sum_d//2 == 0 and cnt //2 != 0:
                flag = False
            
            if flag:
                for k in [0,2,4,6]:
                    nhorse.append([nr,nc,sum_m//5,sum_s//cnt,k])
            
            else:
                for k in [1,3,5,7]:
                    nhorse.append([nr,nc,sum_m//5,sum_s//cnt,k])

    horse = copy.deepcopy(nhorse)
    print(horse)
    tcnt+=1

answer = 0

for i in range(len(horse)):
    answer += horse[i][2]
print(answer)


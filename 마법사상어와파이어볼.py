## 마법사 상어가 크기

## 말의 갯수가 유동적이다.

## 로직

"""
이동 후  같은 위치 말이 2개 이상이면 -> 파이어볼을 나눈다.
 1) 모든 말 이동 
     - 이동 방법
     말들이 있는 위치에서 이동 위치를 탐색
     이동 위치 딕셔너리에 방향과 무게 저장

     - 저장 방법?
     말들의 순서는 중요하지 않다.
     위치 : 말의 정보(방향,무게)

 2) 같은 위치에 있는 말 찾기 
    - 딕셔너리로 말의 갯수가 2개 이상인 위치 탐색

 3) 같은 위치에 있는 말들을 나누기
    - 딕셔너리에 저장되어 있는 말들의 정보를 모두 삭제하고 다시 저장

"""
import copy

horse = []

N,M,K = map(int, input().split())

horse = []
## r,c,m,s(거리),d(속력)
for i in range(M):
    r,c,m,s,d = map(int, input().split())
    horse.append([r-1,c-1,m,s,d])
   

dxy = [[-1,0],[-1,1],[0,1], [1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

tcnt = 0

# cnt가 K번 실행
while tcnt < K:
    ## 같은 위치에 있는 말 찾기
    
    loca = dict()
    ## 말 이동
    for r,c,m,s,d in horse: 
        if m == 0:
            continue
        
        
        nr,nc = r +dxy[d][0]*s, c+dxy[d][1]*s
        
        ## 위치 인덱스 잘못 품
        nr = (nr + N) % N
        nc = (nc + N) % N
    

        if (nr,nc) in loca.keys():
            loca[(nr,nc)].append([m,s,d])

        else:
            loca[(nr,nc)] = [[m,s,d]]
    
    nhorse = []
  
    ## 말들을 나누는 과정
    for r,c in loca.keys():
        ## 질량의 합, 속력의 합, 파이어볼 갯수
        if len(loca[(r,c)]) < 2:
            nhorse.append([r,c]+loca[(r,c)][0])

        elif len(loca[(r,c)]) >= 2:
            cnt_horse = len(loca[(r,c)]) ## 말들의 갯수
            sum_w, sum_v, sum_d,cnt_odd, cnt_even = 0,0,0,0,0
            for m,s,d in loca[(r,c)]:
                sum_w += m  
                sum_v += s
                sum_d += d
                if d % 2 == 0:
                    cnt_even += 1
                else:
                    cnt_odd += 1

                ## 합쳐진 파이어볼 방향이 모두 홀수인지 짝수인지, 짝수이면 
            if cnt_horse ==  cnt_even or cnt_horse ==  cnt_odd:
                for k in [0,2,4,6]:
                    nhorse.append([r,c,sum_w//5,sum_v//cnt_horse,k])
                
            else:
                for k in [1,3,5,7]:
                    nhorse.append([r,c,sum_w//5,sum_v//cnt_horse,k])

    horse = copy.deepcopy(nhorse)
    tcnt+=1

answer = 0


for r,c,m,s,d in nhorse:
    answer += m


print(answer)


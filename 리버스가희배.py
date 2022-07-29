import tabnanny


T = int(input())
orders = list(map(int, input().split()))

start_time = [float("Inf")]*(T+1) 
end_time = [float("-Inf")]*(T+1)  
priority_li = [0]*(T+1)
times = [0]*(T+1)

time = 0
before = 0
priority = 1

## 시간 구하기
for t in orders:
    # print(t, priority)

    times[t] += 1
    if before >= t:
        priority += 1 ## 갯수 구하기 오름차순
    before= t


process_li = []
before = 0
for t in orders:
    if before >= t:
        priority -= 1
    if priority_li[t] == 0:
        priority_li[t] = priority
    


for t in range(1,T+1):
    if times[t]!=0:
        print(t, priority_li[t], times[t] )



        



    
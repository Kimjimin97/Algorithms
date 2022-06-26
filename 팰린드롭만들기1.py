from collections import deque
alpha='ABCDEFGHIJKLNMOPQRSTUVWXYZ'
hash=dict()

for c in alpha:
    hash[c]=0


    
s=input()
if len(s)==0:
    print("")
    exit(0)


for c in s:
    hash[c]+=1

cnt=0
answer=deque([])

for num in hash.values():
    if num%2!=0:
        cnt+=1
if cnt>1:
    print("I'm Sorry Hansoo")

else:
    middle=""
    for a in reversed(alpha):
        n=hash[a]
        if n%2==1:
            middle=a
            
        for j in range(n//2):
            answer.appendleft(a)
            answer.append(a)

    if middle!="":
        answer.insert(len(answer)//2,middle)
    print("".join(answer))
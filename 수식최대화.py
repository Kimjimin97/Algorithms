from itertools import permutations
from collections import deque
import copy
def solution(expression):
    before = deque()
    after = deque()
    
    items = list(permutations(["+","-","*"]))
    
    
    int_str = ""
    origin = deque()
    for s in expression:
        if s in "-+*":
            origin.append(int(int_str))
            origin.append(s)
            int_str = ""
        else:
            int_str += s
            
    origin.append(int(int_str))


    def calculate(left, right, oper):
        if oper == "+":
            value = left + right
            return value
        elif oper =="-":
            value = left - right
            return value
        elif oper =="*":
            value = left * right
            return value
    answer = float("-Inf")
    

    
    for it in items:
        after = origin.copy()
        for oper in it:
            cnt = 0
            before = after.copy()
            after = deque()
            max_len =len(before)
            while cnt < max_len:
                left = before.popleft()
                cnt += 1
                if left == oper:
                    after.append(calculate(after.pop(), before.popleft(),left))
                    cnt += 1
                else:
                    after.append(left)
                    
                    
        
        answer = max(answer, abs(after[0]))
    return 


solution("100-200*300-500+20")
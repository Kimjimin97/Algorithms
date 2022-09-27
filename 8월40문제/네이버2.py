from itertools import product
def solution(users, emoticons):
    answer_lists = []
    candidate = list(product([10,20,30,40],repeat=len(emoticons)))

    

    for c_lists in candidate:
        answer = [0,0]
        for u_ratio, u_money in users:
            money = 0
            for c in range(len(emoticons)):
    
                if u_ratio <= c_lists[c]:
                    money += emoticons[c]*(1-c_lists[c]*0.01)

            if money >= u_money:
                answer[0] += 1
            else:
                answer[1] += money

   
        answer_lists.append(answer)
    answer_lists.sort(reverse=True)
    print(answer_lists)

        
    return answer_lists[0]

print(solution([[40, 2900]],[1300, 1500, 1600, 4900]))

lists = [[100,10],[100,20]]
lists.sort()
print(lists)
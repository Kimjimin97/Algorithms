"""
일부 선수들은 이전에 같은 팀에 속했습니다. 
이 선수들이 모두 팀에 포함될 경우 팀의 숙련도가 2배가 됩니다.
"""

def solution(skills, team, k):
    answer = 0
    N = len(skills)
    i = 0
    j = k-1
    max_score = sum(skills[i:j+1])
    score = sum(skills[i:j+1])
    min_team = min(team) -1
    max_team = max(team) -1
    

    while True: 
        j+=1
        if j == N:
            break
        

        score += skills[j]
        score -= skills[i]

        ## 모두 팀에 들어았는지 확인
        double = False
        if (min_team >= i+1 ) and  (j >= max_team):
            double = True
            score *= 2
            max_score = max(max_score, score)
        else:
            max_score = max(max_score, score)

        if double:
            score //=2
        i+=1
        
        
    return max_score
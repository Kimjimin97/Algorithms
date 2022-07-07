N = int(input())

K = list(map(int, input().split()))

left = 0 
right = N-1
person = N-2
answer = float("-Inf")

while left < right:
    answer = max(answer, person*min(K[left],K[right]))

    if K[left] < K[right]:
        left += 1
    else:
        right -=1
    person -= 1

print(answer)
def solution(nums):
    answer = 0

    s_num = str(nums)
    nums_half_pos = len(s_num) // 2

    if sum(map(int, s_num[:nums_half_pos])) == sum(map(int, s_num[nums_half_pos:])) :
        answer = "LUCKY"
    else:
        answer = "READY"


    return answer



print(solution(123402))
print(solution(7755))

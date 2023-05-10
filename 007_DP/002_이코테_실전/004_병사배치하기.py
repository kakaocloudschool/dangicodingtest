def solution(N, soldiers):
    answer = 0
    pre_v = 0
    dp = [1] * len(soldiers)

    for i in range(len(soldiers) -1, -1, -1) :
        for j in range(len(soldiers) - 1, i, -1):
            if soldiers[j] < soldiers[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


print(solution(7, [15, 14, 8, 5, 2, 4]))
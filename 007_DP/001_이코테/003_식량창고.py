def solution(N, jobs):
    answer = 0
    dp = [0] * len(jobs)
    dp[0] = jobs[0]
    dp[1] = max(jobs[0], jobs[1])

    for i in range(2, len(dp)):
        dp[i] = max(dp[i - 1], dp[i - 2] + jobs[i])

    return dp[-1]


print(solution( 4, [1, 3, 1, 5]))
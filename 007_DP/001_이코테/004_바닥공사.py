def solution(N):
    answer = 0
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 3
    dp[3] = dp[2] + dp[1] * 2
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2] * 2

    return dp[N]


print(solution(4))



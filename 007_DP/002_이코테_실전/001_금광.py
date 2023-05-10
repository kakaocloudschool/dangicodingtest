def solution(n, m, gold_cave):
    answer = 0
    dp = [[0] * 3 for _ in range(4)]
    for i in range(n):
        dp[0][i] = gold_cave[0][i]

    for i in range(1, m):
        print(dp)
        for j in range(n):
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + gold_cave[i][j], )
            if j + 1 < n:
                dp[i][j] = max(dp[i][j], dp[i - 1][j + 1] + gold_cave[i][j], )
            if j - 1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + gold_cave[i][j])
    print(dp)
    return max(dp[-1])



print(solution(3, 4, [[1, 2, 0], [3, 1, 6], [3, 4, 4], [2, 1, 7]]))
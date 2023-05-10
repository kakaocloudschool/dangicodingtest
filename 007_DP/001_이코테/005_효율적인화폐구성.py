def solution(N, M, coin_type):
    answer = 0
    INF = 9876543210
    dp = [INF] * (M + 1)
    for coin in coin_type:
        if coin <= M:
            dp[coin] = 1
    for i in range(1, M + 1):
      if dp[i] != INF:
          continue
      for coin in coin_type:
          if i - coin >= 0 and dp[i - coin] != INF:
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[M] == INF:
        return -1
    else:
        return dp[M]


print(solution(2, 15, [2, 3]))
print(solution(3, 4, [3, 5, 7]))


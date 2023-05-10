# 피보나치 100 값 구하기

dp = [1] * 101

for i in range(3, 101):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[3])


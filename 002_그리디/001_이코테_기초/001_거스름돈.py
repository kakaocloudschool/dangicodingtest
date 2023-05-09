N = 1260
coin_type = [500, 100, 50, 10]

answer = 0

for coin in coin_type:
    coin_cnt = N // coin
    N = N - coin * coin_cnt
    answer += coin_cnt

print(answer)
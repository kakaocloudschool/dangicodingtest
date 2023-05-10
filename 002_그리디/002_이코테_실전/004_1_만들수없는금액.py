# 315p 체크 필요.
import itertools

N = int(input())
coins = list(map(int, input().split()))

answer = sum(coins) + 1
coin_v = [0] * (sum(coins) + 1)

for i in range(N):
    for j in itertools.permutations(coins,i + 1):
        coin_v[sum(j)] = 1

for i in range(1, len(coin_v)):
    if coin_v[i] == 0:
        answer = i
        break

print(answer)





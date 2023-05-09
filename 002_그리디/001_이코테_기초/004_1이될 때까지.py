N, K = map(int, input().split())
answer = 0
namuge = 0
while(N >= K):
    mok = N // K
    namuge = N % K
    answer += namuge + 1
    N = mok
answer += N - 1

print(answer)

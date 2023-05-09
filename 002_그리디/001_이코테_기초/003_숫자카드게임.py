N, M = map(int, input().split())
NUM_LIST = []
answer = 0
for _ in range(N):
    v = list(map(int, input().split()))
    answer = max(answer, min(v))

print(answer)
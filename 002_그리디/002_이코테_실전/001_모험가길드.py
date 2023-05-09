N = int(input())
T_G = list(map(int, input().split()))

T_G.sort()

answer = 0
wait = 0

for travel in T_G:
    if wait + 1 >= travel:
        wait = 0
        answer += 1
    else:
        wait += 1

print(answer)
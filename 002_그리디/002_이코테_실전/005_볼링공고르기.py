import itertools

N, M = map(int, input().split())
boling_gongs = list(map(int, input().split()))

answer = 0

for i in range(len(boling_gongs)):
    for j in range(i + 1, len(boling_gongs)):
        if boling_gongs[i] != boling_gongs[j]:
            answer += 1

print(answer)

"""
5 3
1 3 2 3 2

8
"""
"""
8 5
1 5 4 3 2 4 5 2

25
"""

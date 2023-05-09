N = int(input())

answer = 0

for i in range(N + 1):
    if i % 10 == 3:
        answer += 3600
    else:
        for j in range(60):
            if j % 10 == 3 or j // 10 == 3:
                answer += 60
            else:
                for k in range(60):
                    if k % 10 == 3 or k // 10 == 3:
                        answer += 1

print(answer)




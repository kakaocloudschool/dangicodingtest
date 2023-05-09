cnt = int(input())

n_score = {}

for i in range(cnt):
    name, score  = input().split()
    n_score[name] = score

a = sorted(n_score.items() , key=lambda x: x[1])

for name in a:
    print(name[0], end= ' ')
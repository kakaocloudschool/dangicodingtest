cnt = int(input())

num_list = []

for _ in range(cnt):
    num_list.append(int(input()))

num_list.sort(reverse=True)
for num in num_list:
    print(num, end=' ')

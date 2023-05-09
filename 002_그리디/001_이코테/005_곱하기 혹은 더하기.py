str_num = input()
answer = 0
for num in str_num:
    i = int(num)
    if i < 2 or answer < 2:
        answer += i
    else:
        answer *= i

print(answer)
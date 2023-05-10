S = input()

zero_group_cnt = 0
one_group_cnt = 0

bef = 'n'
for c in S:
    if c != bef:
        if c == '0':
            zero_group_cnt += 1
        else:
            one_group_cnt += 1
        bef = c

answer = min(zero_group_cnt, one_group_cnt)

print(answer)
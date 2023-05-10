# 324 p [리트 필요]

def solution(s):
    answer = len(s)
    for i in range(1, (len(s) // 2 + 1)):
        tmp_comp = ""
        tmp_pre = s[0:i]
        tmp_cnt = 1

        for j in range(i, len(s), i):
            if tmp_pre == s[j: j + i]:
                tmp_cnt += 1
            else:
                if tmp_cnt >= 2:
                    tmp_comp += str(tmp_cnt) + tmp_pre
                else:
                    tmp_comp += tmp_pre
                tmp_pre = s[j:j + i]
                tmp_cnt = 1

        if tmp_cnt >= 2:
            tmp_comp += str(tmp_cnt) + tmp_pre
        else:
            tmp_comp += tmp_pre
        print(tmp_comp)
        answer = min(answer, len(tmp_comp))


    return answer


print(solution("aabbaccc"))
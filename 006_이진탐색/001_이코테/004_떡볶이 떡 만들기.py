def cut_length(array, length):
    cut_len = 0
    for eliement in array:
        cut_len += max(eliement - length, 0)
    return cut_len

def binary_search(array, target,  start, end, tmp):
    while (start <= end):
        mid = (start + end) // 2
        cut_len = cut_length(array, mid)

        if cut_len == target:
            return mid
        elif cut_len > target:
            start = mid + 1
        else:
            tmp = mid
            end = mid - 1
    return tmp

def solution(N, M, dduks):
    answer = binary_search(dduks, M, 0, max(dduks), -1)
    return answer


print(solution(4, 6, [19, 15, 10 ,17]))
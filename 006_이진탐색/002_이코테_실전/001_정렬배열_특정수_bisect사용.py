from bisect import bisect_left, bisect_right

def count_by_range(array, left_v, right_v):
    right_index = bisect_right(array,right_v)
    left_index = bisect_left(array, left_v)
    return right_index - left_index

def solution(N, M, NUM_LIST):
    answer = count_by_range(NUM_LIST, M, M)
    if answer == 0:
        return -1
    else:
        return answer


print(solution(7, 2, [1, 1, 2, 2, 2, 2, 3]))
print(solution(7, 4, [1, 1, 2, 2, 2, 2, 3]))


n , x = map(int, input())
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


def solution(N, M, NUM_LIST):
    answer = 0

    pos = binary_search(NUM_LIST, M, 0, N - 1)
    if pos is None:
        return -1

    for i in range(pos, 0, -1):
        if NUM_LIST[i] == M:
            answer += 1
        else:
            break

    for i in range(pos + 1, len(NUM_LIST)):
        if NUM_LIST[i] == M:
            answer += 1
        else:
            break

    return answer





print(solution(7, 2, [1, 1, 2, 2, 2, 2, 3]))
print(solution(7, 4, [1, 1, 2, 2, 2, 2, 3]))

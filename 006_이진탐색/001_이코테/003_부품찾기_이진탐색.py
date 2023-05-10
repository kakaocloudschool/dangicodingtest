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


def solution(N, items, R, r_items ):

    answer = []
    items.sort()
    for r_item in r_items:
        if binary_search(items, r_item, 0, len(items) - 1) is None:
            answer.append("no")
        else:
            answer.append("yes")

    return answer

print(solution(5, [8, 3, 7, 9 ,2], 3, [5, 7, 9]))


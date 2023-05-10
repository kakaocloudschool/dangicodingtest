def solution(N, items, R, r_items ):
    answer = ["no"] * len(r_items)
    for item in items:
        for j in range(len(r_items)):
            if item == r_items[j]:
                answer[j] = "yes"

    return answer


print(solution(5, [8, 3, 7, 9 ,2], 3, [5, 7, 9]))


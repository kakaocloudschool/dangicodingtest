def solution(food_times, k):
    answer = 0
    pos = 0

    for i in range(k):
        if food_times[pos] != 0:
            food_times[pos] -= 1
            pos = (pos + 1) % len(food_times)
        else:
            for j in range(1, len(food_times)):
                alt_pos = (pos + j) % len(food_times)
                if food_times[alt_pos] != 0:
                    food_times[alt_pos] -= 1
                    pos = (alt_pos + 1) % len(food_times)
    answer = pos + 1

    return answer


result = solution([3, 1, 2], 5)
if result == 1:
    print("정답")
else:
    print(f"출력 결과 : {result} 오답 (정답 : 1)")


# 데이터가 정렬된 상태에서 특정 데이터를 탐색할 떄 사용

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

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("존재하지 않는 데이터 ")
else:
    print(result + 1)
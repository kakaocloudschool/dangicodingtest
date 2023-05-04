a = [1 ,2 ,3 ,4 ,5]
print(a)

print(a[3])

n = 10
a = [0] * n
a[0] = 1
print(a)


array = [i for i in range(10)]
print(array)

# 리스트 컴프리 핸션
# 이 방식을 사용하지 않고 단순히 나타내면 콜바이 레퍼런스로 변해서, 데이터 전체가 변하게 된다.
array_2 = [[0] * 10 for _ in range(10) ]
array_2[0][0] = 1

# 리스트 에서 특정 값 제거하기
a = [1, 2, 3, 4, 5, 5]
remove_set = {3, 5}

answer = [i for i in a if i not in remove_set ]

print(answer)
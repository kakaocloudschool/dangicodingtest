# N : 덧셈 가능한 숫자의 개수
# M : 최종 결과에 더해진 수
# K :
N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))
answer = 0

num_list.sort(reverse=True)


mok = M // (K + 1)
namuge = M % (K + 1)
answer += num_list[0] * (K * mok + namuge)
answer += num_list[1] * (mok)

print(answer)

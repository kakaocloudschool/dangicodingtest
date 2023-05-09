N, M = map(int, input().split())
ice_map = []
answer = 0

def dfs(ice_map, x, y):
    if ice_map[x][y] == 1:
        return False
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    ice_map[x][y] = 1
    for add_x, add_y in moves:
        move_x = add_x + x
        move_y = add_y + y
        if 0 <= move_x < N and 0 <= move_y < M:
            dfs(ice_map, move_x, move_y)
    return True

for i in range(N):
    ice_map.append(list(map(int, input())))

for i in range(N):
    for j in range(M):
        if dfs(ice_map, i, j):
            print(ice_map, i, j)
            answer += 1

print(answer)

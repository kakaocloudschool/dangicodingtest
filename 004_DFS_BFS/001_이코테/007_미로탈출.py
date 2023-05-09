def solution():
    N, M = map(int, input().split())
    mon_map = []
    for _ in range(N):
        mon_map.append(list(map(int, input())))

    def dfs(mon_map, x, y, cost):
        if mon_map[x][y] != 1:
            return 9999
        mon_map[x][y] = cost
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        cost = cost + 1
        for move in moves:
            move_x = move[0] + x
            move_y = move[1] + y
            if 0 <= move_x < N and 0 <= move_y < M:
                dfs(mon_map, move_x, move_y, cost)

    dfs(mon_map, 0, 0, 1)
    print(mon_map[N - 1][M - 1])

solution()
"""
5 6
101010
111111
000001
111111
111111
"""
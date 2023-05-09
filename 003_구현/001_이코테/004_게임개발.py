max_x, max_y = map(int, input().split())
x, y, arrow = map(int, input().split())

gamemap = []
answer = 1

arrows = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for i in range(max_x):
    gamemap.append(list(map(int, input().split())))

cnt = 0
while(True):
    if cnt == 4:
        break

    add_x , add_y = arrows[arrow]
    move_x = add_x + x
    move_y = add_y + y

    if move_x < 0 or move_x >= max_x or move_y < 0 or move_y >= max_y:
        arrow = (arrow + 1) % 4
        cnt += 1

    if gamemap[move_x][move_y] == 1:
        arrow = (arrow + 1) % 4
        cnt += 1
    else:
        gamemap[move_x][move_y] = 1
        answer += 1
        x = move_x
        y = move_y
        cnt = 0

print(answer)
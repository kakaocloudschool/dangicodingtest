size = int(input())
move_list = input().split()

add_xy = {"U": [-1, 0], "D": [1, 0], "R": [0, 1], "L": [0, -1]}
x = 1
y = 1

for move in move_list:
    add_x, add_y = add_xy[move]
    if 1 <= add_x + x <= size and 1 <= add_y + y <= size:
        x = add_x + x
        y = add_y + y

print(x, y)
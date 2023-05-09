location = input()
chess_size = 8

x = ord(location[0]) - ord('a') + 1
y = int(location[1])

moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
answer = 0

for add_x, add_y in moves:
    if 0 < x + add_x <=chess_size and 0 < y + add_y <= chess_size:
        answer += 1

print(answer)



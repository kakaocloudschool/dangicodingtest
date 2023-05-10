questions = input()

char_arr = []
num = 0
for c in questions:
    if "A" <= c <= "Z":
        char_arr.append(c)
    else:
        num += int(c)


char_arr.sort()

print(('').join(char_arr) + str(num))

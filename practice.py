# matrix = [
#     ['.', '*', '*'],
#     ['*', '.', '.'],
#     ['.', '*', '.'],
# ]
#
# col = 3
# row = 3
row = input()
col = input()

matrix = []
for i in range(row):
    matrix.append(list(col))

for y_idx, y in enumerate(matrix):
    # print(y_idx, y)
    # print(y)
    for x_idx, x in enumerate(y):
        # print(f'x: {x}')
        # print(x_idx, x, end="\t")
        # print(f'x: {x},,,, {x_idx}, {y_idx}')
        if x == '.':
            count = 0

            y_start = y_idx-1 if 0 <= y_idx-1 else 0
            y_end = y_idx+1 if y_idx+1 <= row-1 else row-1
            x_start = x_idx-1 if 0 <= x_idx-1 else 0
            x_end = x_idx+1 if x_idx+1 <= col-1 else col-1
            # print(f'x: {x},,,, {x_idx}, {y_idx}')
            # print(f'x: {x_start}, {x_end}')
            # print(f'y: {y_start}, {y_end}')
            for j in range(y_start, y_end+1):
                for i in range(x_start, x_end+1):
                    print(matrix[i][j])
                    if matrix[j][i] == '*':
                        count += 1

            # print(f'save count in ({x_idx}, {y_idx}) number {count}')
            matrix[y_idx][x_idx] = count

            # print(matrix)
            
        

# print(matrix)
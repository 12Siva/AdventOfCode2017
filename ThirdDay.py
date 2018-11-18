NORTH, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)  # directions
turn_right = {NORTH: E, E: S, S: W, W: NORTH}  # old -> new direction
turn_left = {NORTH: W, E: NORTH, S: E, W: S}  # old -> new direction


def spiral(width, height):
    if width < 1 or height < 1:
        raise ValueError
    x, y = width // 2, height // 2  # start near the center
    dx, dy = NORTH  # initial direction
    matrix = [[None] * width for _ in range(height)]
    count = 0
    while True:
        count += 1

        if (count == 1):
            matrix[y][x] = count  # visit
        else:
            matrix[y][x] = getVal(matrix, y, x, width, height)  # visit

        # try to turn left
        if (count == 1):
            new_dx, new_dy = E
        else:
            new_dx, new_dy = turn_left[dx, dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
                    matrix[new_y][new_x] is None):  # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else:  # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix  # nowhere to go


def getVal(matrix, y, x, width, height):
    val = 0
    print(matrix[1][2])

    a = x - 1
    b = x + 1
    c = y - 1
    d = y + 1

    if (a > width) and (matrix[y][a] != None):
        val = val + matrix[y][a]
    if (b > width) and (matrix[y][b] != None):
        val = val + matrix[y][b]

    if (c > height) and (matrix[c][x] != None):
        val = val + matrix[c][x]
    if (d > height) and (matrix[d][x] != None):
        val = val + matrix[d][x]

    if (a > width) and (d > height) and (matrix[d][a] != None):
        val = val + matrix[d][a]
    if (b > width) and (d > height) and (matrix[d][b] != None):
        val = val + matrix[d][b]

    if (a > width) and (c > height) and (matrix[c][a] != None):
        val = val + matrix[c][a]
    if (b > width) and (c > height) and (matrix[c][b] != None):
        val = val + matrix[c][b]

    return val


def print_matrix(matrix):
    width = len(str(max(el for row in matrix for el in row if el is not None)))
    fmt = "{:0%dd}" % width
    for row in matrix:
        print(" ".join("_" * width if el is None else fmt.format(el) for el in row))


matrix = spiral(3, 3)
print_matrix(matrix)
arr = []
for x in range(0, len(matrix)):
    smallList = matrix[x]
    tmp = []
    for y in range(0, len(smallList)):
        if (smallList[y] != None):
            tmp.append(smallList[y])
    if (tmp != []):
        arr.append(tmp)

x1 = 0
y1 = 0
x361527 = 0
y361527 = 0

for x in range(0, len(arr)):
    smallList = arr[x]
    for y in range(0, len(smallList)):
        if (smallList[y] == 1):
            x1 = y + 1
            y1 = x + 1
        elif (smallList[y] == 361527):
            x361527 = y + 1
            y361527 = x + 1

manhattan_distance = abs(x361527 - x1) + abs(y361527 - y1)

print(manhattan_distance)

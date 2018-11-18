def setup():
    arr = []
    with open("input.txt") as fileobj:
        for line in fileobj:
            arr.append(int(line.rstrip()))

    return arr

def getCountToEscape(inputList):
    count = 0
    index = 0
    while index < len(inputList):
        count = count + 1
        jump = inputList[index] # Represents the current value

        # Part 1
        # inputList[index] = jump + 1

        # Part 2
        if (jump >= 3):
            inputList[index] = jump - 1
        else:
            inputList[index] = jump + 1

        index = index + jump

    return count



if __name__ == '__main__':
    arr = setup()
    # arr = [0, 3, 0, 1, -3] # Test Case Input
    result = getCountToEscape(arr)
    print(result)
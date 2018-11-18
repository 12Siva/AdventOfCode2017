import operator

def setup():
    arr = []
    with open("input.txt") as fileobj:
        for line in fileobj:
            tmp = line.split("\t")

    tmp = [int(ele) for ele in tmp]
    return tmp


def part1(inputList):
    list = inputList
    count = 1
    seen = {}
    seen[tuple(inputList)] = 1
    while True:
        print(tuple(list))
        max_index, max_value = max(enumerate(inputList), key=operator.itemgetter(1))



        if seen.__contains__(tuple(list)):
            print("FINAL")
            print(tuple(list))
            return count
        else:
            seen[tuple(list)] = 1

        count = count + 1


if __name__ == '__main__':
    arr = setup()
    #arr = [0, 2, 7, 0]
    print(part1(arr))

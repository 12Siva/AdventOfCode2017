def setup():
    arr = []
    with open("input.txt") as fileobj:
        for line in fileobj:
            for ch in line:
                s = line.split("\t")
                tmp = []
                for ele in s:
                    tmp.append(int(ele.rstrip()))
            arr.append(tmp)
    return arr


def part1(arr):
    diff = []

    for x in range(0, len(arr)):
        m = min(arr[x])
        m1 = max(arr[x])
        diff.append(m1 - m)

    print(diff)
    print(sum(diff))


def part2(arr):
    div = []
    for x in range(0, len(arr)):
        smallList = arr[x]
        for y in range(0, len(smallList)):
            val1 = smallList[y]
            for z in range(y+1, len(smallList)):
                val2 = smallList[z]
                if (val1 % val2 == 0):
                    div.append(val1 / val2)
                if (val2 % val1 == 0):
                    div.append(val2 / val1)

    print(div)
    print(sum(div))



if __name__ == '__main__':
    arr = setup()
    #arr = [[5,9,2,8],[9,4,7,3],[3,8,6,5]]
    part2(arr)

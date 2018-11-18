import operator

ops = { "inc": operator.add,
        "dec": operator.sub,
        ">": operator.gt,
        ">=": operator.ge,
        "<": operator.lt,
        "<=": operator.le,
        "==": operator.eq,
        "!=": operator.ne}

def setup():
    arr = []
    with open("input.txt") as fileobj:
        for line in fileobj:
            arr.append(line.rstrip())

    return arr

def part1(inputList):
    registerValues = {}

    tmpMaxVal = 0
    for inst in inputList:
        ins = inst.split(" ")

        currRegister = ins[0]
        currIns = ins[1]
        currRegisterVal = int(ins[2])

        referenceRegister = ins[4]
        referenceOperation = ins[5]
        referenceVal = int(ins[6])

        operator = ops[referenceOperation]

        if not (registerValues.__contains__(referenceRegister)):
            registerValues[referenceRegister] = 0
        if not (registerValues.__contains__(currRegister)):
            registerValues[currRegister] = 0

        if (operator(registerValues[referenceRegister], referenceVal)):
            op = ops[currIns]
            val = op(registerValues[currRegister], currRegisterVal)
            registerValues[currRegister] = val
            if (val >= tmpMaxVal):
                tmpMaxVal = val

    return tmpMaxVal

if __name__ == '__main__':
    arr = setup()
    registerValues = part1(arr)
    #print(registerValues) FOR PART 1
    #print(max(tuple(registerValues.values()))) FOR PART 1
    print(registerValues)
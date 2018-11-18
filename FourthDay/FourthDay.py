from collections import Counter

def setup():
    arr = []
    with open("input.txt") as fileobj:
        for line in fileobj:
            s = line.split("\t")
            temp = s[0].split(" ")
            tmp = []
            for ele in temp:
                tmp.append(ele.rstrip())
            arr.append(tmp)

    return arr

def is_anagram(str1, str2):
   return Counter(str1) == Counter(str2)

def isValidPart1(inputList):
    #  CAN BE DONE WITH A HASHMAP
    for x in range(0, len(inputList)):
        tmp = inputList[x]
        for y in range(x+1, len(inputList)):
            if (inputList[y] == tmp):
                #print(inputList)
                return False;
    return True

def isValidPart2(inputList):
    for x in range(0, len(inputList)):
        tmp = inputList[x]
        for y in range(x+1, len(inputList)):
            if (is_anagram(tmp, inputList[y])):
                #print(inputList)
                return False;
    return True



if __name__ == '__main__':
    arr = setup()
    count = 0
    for passPhrase in arr:
        if isValidPart1(passPhrase) and isValidPart2(passPhrase):
            count = count + 1

    print(count)

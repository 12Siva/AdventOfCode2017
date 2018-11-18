# http://adventofcode.com/2017/day/1
# Part 1
# arr = []
#
# with open("FirstDay/input.txt") as fileobj:
#     for line in fileobj:
#        for ch in line:
#            if ch != '\n':
#             arr.append(int(ch))
#
# match = []
#
# for x in range(0, len(arr)-1):
#     if (arr[x] == arr[x+1]):
#         match.append(arr[x])
#
# last = arr[len(arr)-1]
# first = arr[0]
# if (last == first):
#     match.append(last)
#
# print(match)
# print(sum(match))

# Part 2
arr = []

with open("FirstDay/input.txt") as fileobj:
    for line in fileobj:
       for ch in line:
           if ch != '\n':
            arr.append(int(ch))

match = []

s = len(arr)
jump = int(s / 2)
print(jump)

for x in range(0, jump):
    if (arr[x] == arr[x + jump]):
        match.append(arr[x])

for x in range(jump, s):
    if (arr[x] == arr[x - jump]):
        match.append(arr[x])

print(match)
print(sum(match))
